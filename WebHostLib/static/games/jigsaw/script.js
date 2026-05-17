"use strict";

window.pieceSides = 4;
const corner_to_shape_dist = 1/3; // distance from corner to shape in hexagonal piece

window.downsize_to_fit = 0.85;
window.show_clue = true;
window.rotations = 0;
window.zero_list = [0,0];

var accept_pending_actions = false;
var process_pending_actions = false;

var bevel_size = localStorage.getItem("option_bevel_2");
if (bevel_size === null) bevel_size = 0.1;

var shadow_size = localStorage.getItem("option_shadow_2");
if (shadow_size === null) shadow_size = 0;

// Set starting values from localStorage or defaults
document.addEventListener('DOMContentLoaded', function() {
    const borderSelect = document.getElementById('options_bt');
    const shadowSelect = document.getElementById('options_st');

    // Load from localStorage or use default
    function formatValue(val, def) {
        val = parseFloat(localStorage.getItem(val));
        if (isNaN(val)) val = def;
        return (val % 1 === 0) ? val.toString() : val.toFixed(1);
    }
    borderSelect.value = formatValue('option_bevel_2', 0.1);
    shadowSelect.value = formatValue('option_shadow_2', 0);

    // Save to localStorage on change
    borderSelect.addEventListener('change', function() {
        localStorage.setItem('option_bevel_2', borderSelect.value);
    });
    shadowSelect.addEventListener('change', function() {
        localStorage.setItem('option_shadow_2', shadowSelect.value);
    });
});

let allow_zoom = true;
const zoomBtn = document.getElementById('m11a');
zoomBtn.addEventListener('click', function() {
    allow_zoom = !allow_zoom;
    zoomBtn.innerHTML = allow_zoom ? '🔍✅' : '🔍❌';
});


window.save_loaded = false;
window.ignore_bounce_pieces = [];

var puzzle;

let seed = 1;

function random() {
    const x = Math.sin(seed++) * 10000;
    return x - Math.floor(x);
}

function randomIn(inputNumber) {
    return Math.abs(Math.sin(inputNumber * inputNumber));
}

function setRandomSeed(newSeed) {
    if (typeof newSeed === 'number') {
        seed = newSeed;
    }
}

const mhypot = Math.hypot,
    mrandom = random,
    mmax = Math.max,
    mmin = Math.min,
    mround = Math.round,
    mfloor = Math.floor,
    msqrt = Math.sqrt,
    mabs = Math.abs;
//-----------------------------------------------------------------------------

function alea(min, max) {
    // random number [min..max[ . If no max is provided, [0..min[

    if (typeof max == 'undefined') return min * mrandom();
    return min + (max - min) * mrandom();
}

// - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

function intAlea(min, max) {
    // random integer number [min..max[ . If no max is provided, [0..min[

    if (typeof max == 'undefined') {
    max = min; min = 0;
    }
    return mfloor(min + (max - min) * mrandom());
} // intAlea

//-----------------------------------------------------------------------------

// Point - - - - - - - - - - - - - - - - - - - -
class Point {
    constructor(x, y) {
    this.x = Number(x);
    this.y = Number(y);
    } // constructor
    copy() {
    return new Point(this.x, this.y);
    }

    distance(otherPoint) {
    return mhypot(this.x - otherPoint.x, this.y - otherPoint.y);
    }
} // class Point

// Segment - - - - - - - - - - - - - - - - - - - -
// those segments are oriented
class Segment {
    constructor(p1, p2) {
    this.p1 = new Point(p1.x, p1.y);
    this.p2 = new Point(p2.x, p2.y);
    }
    dx() {
    return this.p2.x - this.p1.x;
    }
    dy() {
    return this.p2.y - this.p1.y;
    }
    length() {
    return mhypot(this.dx(), this.dy());
    }

    // returns a point at a given distance of p1, positive direction beeing towards p2

    pointOnRelative(coeff) {
    // attention if segment length can be 0
    let dx = this.dx();
    let dy = this.dy();
    return new Point(this.p1.x + coeff * dx, this.p1.y + coeff * dy);
    }
} // class Segment
//-----------------------------------------------------------------------------
// one side of a piece
class Side {
    constructor() {
    this.type = ""; // "d" pour straight line or "z" pour classic
    this.points = []; // real points or Bezier curve points
    // this.scaledPoints will be added when we know the scale
    } // Side

    //- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    //- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    reversed() {
    // returns a new Side, copy of current one but reversed
    const ns = new Side();
    ns.type = this.type;
    ns.points = this.points.slice().reverse();
    return ns;
    } // Side.reversed

    //- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    side_scale(puzzle) {
        /* uses actual dimensions of puzzle to compute actual side points
        these points are not shifted by the piece position : the top left corner is at (0,0)
        */
        const coefx = puzzle.scalex;
        const coefy = puzzle.scaley;
        
        this.scaledPoints = this.points.map(p => new Point(p.x * coefx, p.y * coefy));
    } //

    //- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    /*
    draws the path corresponding to a side
    Parameters :
    ctx : canvas context
    shiftx, shifty : position shift (used to create emboss effect)
    withoutMoveTo : to decide whether to do a moveTo to the first point. Without MoveTo
    must be done only for the first side of a piece, not for the following ones
    */

    drawPath(ctx, shiftx, shifty, withoutMoveTo) {

        if (!withoutMoveTo) {
            ctx.moveTo(this.scaledPoints[0].x + shiftx, this.scaledPoints[0].y + shifty);
        }
        if (this.type == "d") {
            ctx.lineTo(this.scaledPoints[1].x + shiftx, this.scaledPoints[1].y + shifty);
        } else { // edge zigzag
            for (let k = 1; k < this.scaledPoints.length - 1; k += 3) {
                ctx.bezierCurveTo(this.scaledPoints[k].x + shiftx, this.scaledPoints[k].y + shifty,
                    this.scaledPoints[k + 1].x + shiftx, this.scaledPoints[k + 1].y + shifty,
                    this.scaledPoints[k + 2].x + shiftx, this.scaledPoints[k + 2].y + shifty);
            } // for k
        } // if jigsaw side

    } // Side.drawPath
} // class Side

//-----------------------------------------------------------------------------
/* modifies a side
    changes it from a straight line (type "d") to a complex one (type "z")
    The change is done towards the opposite side (side between corners ca and cb)
*/

function twist0(side, ca, cb, howFar = 1) {

    const seg0 = new Segment(side.points[0], side.points[1]);
    const dxh = seg0.dx();
    const dyh = seg0.dy();

    let seg1 = new Segment(ca, cb);
    if(howFar < 1){
        seg1 = new Segment(new Point(howFar * ca.x + (1-howFar) * side.points[0].x, howFar * ca.y + (1-howFar) * side.points[0].y), 
            new Point(howFar * cb.x + (1-howFar) * side.points[1].x, howFar * cb.y + (1-howFar) * side.points[1].y));
    }
    const mid0 = seg0.pointOnRelative(0.5);
    const mid1 = seg1.pointOnRelative(0.5);

    const segMid = new Segment(mid0, mid1);
    const dxv = segMid.dx();
    const dyv = segMid.dy();

    const scalex = alea(0.8, 1);
    const scaley = alea(0.9, 1);
    const mid = alea(0.45, 0.55);

    const pa = pointAt(mid - 1 / 12 * scalex, 1 / 12 * scaley);
    const pb = pointAt(mid - 2 / 12 * scalex, 3 / 12 * scaley);
    const pc = pointAt(mid, 4 / 12 * scaley);
    const pd = pointAt(mid + 2 / 12 * scalex, 3 / 12 * scaley);
    const pe = pointAt(mid + 1 / 12 * scalex, 1 / 12 * scaley);

    side.points = [seg0.p1,
    new Point(seg0.p1.x + 5 / 12 * dxh * 0.52,
    seg0.p1.y + 5 / 12 * dyh * 0.52),
    new Point(pa.x - 1 / 12 * dxv * 0.72,
    pa.y - 1 / 12 * dyv * 0.72),
    pa,
    new Point(pa.x + 1 / 12 * dxv * 0.72,
    pa.y + 1 / 12 * dyv * 0.72),

    new Point(pb.x - 1 / 12 * dxv * 0.92,
    pb.y - 1 / 12 * dyv * 0.92),
    pb,
    new Point(pb.x + 1 / 12 * dxv * 0.52,
    pb.y + 1 / 12 * dyv * 0.52),
    new Point(pc.x - 2 / 12 * dxh * 0.40,
    pc.y - 2 / 12 * dyh * 0.40),
    pc,
    new Point(pc.x + 2 / 12 * dxh * 0.40,
    pc.y + 2 / 12 * dyh * 0.40),
    new Point(pd.x + 1 / 12 * dxv * 0.52,
    pd.y + 1 / 12 * dyv * 0.52),
    pd,
    new Point(pd.x - 1 / 12 * dxv * 0.92,
    pd.y - 1 / 12 * dyv * 0.92),
    new Point(pe.x + 1 / 12 * dxv * 0.72,
    pe.y + 1 / 12 * dyv * 0.72),
    pe,
    new Point(pe.x - 1 / 12 * dxv * 0.72,
    pe.y - 1 / 12 * dyv * 0.72),
    new Point(seg0.p2.x - 5 / 12 * dxh * 0.52,
    seg0.p2.y - 5 / 12 * dyh * 0.52),
    seg0.p2];
    side.type = "z";

    function pointAt(coeffh, coeffv) {
    return new Point(seg0.p1.x + coeffh * dxh + coeffv * dxv,
        seg0.p1.y + coeffh * dyh + coeffv * dyv)
    } // pointAt

} // twist0

//-----------------------------------------------------------------------------
/* modifies a side
    changes it from a straight line (type "d") to a complex one (type "z")
    The change is done towards the opposite side (side between corners ca and cb)
*/

function twist1(side, ca, cb, howFar = 1) {

    const seg0 = new Segment(side.points[0], side.points[1]);
    const dxh = seg0.dx();
    const dyh = seg0.dy();

    let seg1 = new Segment(ca, cb);
    if(howFar < 1){
        seg1 = new Segment(new Point(howFar * ca.x + (1-howFar) * side.points[0].x, howFar * ca.y + (1-howFar) * side.points[0].y), 
            new Point(howFar * cb.x + (1-howFar) * side.points[1].x, howFar * cb.y + (1-howFar) * side.points[1].y));
    }
    const mid0 = seg0.pointOnRelative(0.5);
    const mid1 = seg1.pointOnRelative(0.5);

    const segMid = new Segment(mid0, mid1);
    const dxv = segMid.dx();
    const dyv = segMid.dy();

    const pa = pointAt(alea(0.3, 0.35), alea(-0.05, 0.05));
    const pb = pointAt(alea(0.45, 0.55), alea(0.2, 0.3));
    const pc = pointAt(alea(0.65, 0.78), alea(-0.05, 0.05));

    side.points = [seg0.p1,
    seg0.p1, pa, pa,
    pa, pb, pb,
    pb, pc, pc,
    pc, seg0.p2, seg0.p2];
    side.type = "z";

    function pointAt(coeffh, coeffv) {
    return new Point(seg0.p1.x + coeffh * dxh + coeffv * dxv,
        seg0.p1.y + coeffh * dyh + coeffv * dyv)
    } // pointAt

} // twist1

//-----------------------------------------------------------------------------
/* modifies a side
    changes it from a straight line (type "d") to a complex one (type "z")
    The change is done towards the opposite side (side between corners ca and cb)
*/

function twist2(side, ca, cb, howFar = 1) {

    const seg0 = new Segment(side.points[0], side.points[1]);
    const dxh = seg0.dx();
    const dyh = seg0.dy();

    let seg1 = new Segment(ca, cb);
    if(howFar < 1){
        seg1 = new Segment(new Point(howFar * ca.x + (1-howFar) * side.points[0].x, howFar * ca.y + (1-howFar) * side.points[0].y), 
            new Point(howFar * cb.x + (1-howFar) * side.points[1].x, howFar * cb.y + (1-howFar) * side.points[1].y));
    }
    const mid0 = seg0.pointOnRelative(0.5);
    const mid1 = seg1.pointOnRelative(0.5);

    const segMid = new Segment(mid0, mid1);
    const dxv = segMid.dx();
    const dyv = segMid.dy();

    const hmid = alea(0.45, 0.55);
    const vmid = alea(0.4, 0.5)
    const pc = pointAt(hmid, vmid);
    let sega = new Segment(seg0.p1, pc);

    const pb = sega.pointOnRelative(2 / 3);
    sega = new Segment(seg0.p2, pc);
    const pd = sega.pointOnRelative(2 / 3);

    side.points = [seg0.p1, pb, pd, seg0.p2];
    side.type = "z";

    function pointAt(coeffh, coeffv) {
    return new Point(seg0.p1.x + coeffh * dxh + coeffv * dxv,
        seg0.p1.y + coeffh * dyh + coeffv * dyv)
    } // pointAt

} // twist2

//-----------------------------------------------------------------------------
/* modifies a side
    changes it from a straight line (type "d") to a complex one (type "z")
    The change is done towards the opposite side (side between corners ca and cb)
*/

function twist3(side, ca, cb, howFar = 1) {

    side.points = [side.points[0], side.points[1]];

} // twist3


//-----------------------------------------------------------------------------
class Piece {
    constructor(kx, ky, index) {
        this.sides = [];
        for (let i = 0; i < (window.pieceSides); i++) {
            this.sides[i] = new Side();
        }
        this.kx = kx;
        this.ky = ky;
        this.index = index;
        this.drawn = false;
    }

    //- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    piece_scale(puzzle) {
        this.sides.forEach(side => side.side_scale(puzzle));
    } // Piece.scale
} // class Piece
//--------------------------------------------------------------

function rotateVector(x, y, rotations) {
    if(window.rotations == 0) return {x, y};

    let degree_rotate;
    let num_rots = Math.round(360 / window.rotations);
    if(window.rotations == 180){
        num_rots = 4;
        rotations = (rotations + num_rots) % num_rots; // Ensure rotations are within 0-3
        degree_rotate = rotations * 90;
    }else{
        degree_rotate = rotations * window.rotations;
        rotations = (rotations + num_rots) % num_rots; // Ensure rotations are within 0-3
    }
    
    // Calculate current radius and angle
    const radius = Math.sqrt(x * x + y * y);
    let angle = Math.atan2(-y, x);

    // Add the rotation in radians
    angle += degree_rotate * Math.PI / 180;

    // Convert back to x and y
    x = radius * Math.cos(angle);
    y = -radius * Math.sin(angle);
    return { x, y };
}

//--------------------------------------------------------------
class PolyPiece {

    // represents a group of pieces well positionned with respect  to each other.
    // pckxmin, pckxmax, pckymin and pckymax record the lowest and highest kx and ky
    // creates a canvas to draw polypiece on, and appends this canvas to puzzle.container
    constructor(initialPieces, puzzle) {
        this.pckxmin = Math.min(...initialPieces.map(piece => piece.kx));
        this.pckxmax = Math.max(...initialPieces.map(piece => piece.kx)) + 1;
        this.pckymin = Math.min(...initialPieces.map(piece => piece.ky));
        this.pckymax = Math.max(...initialPieces.map(piece => piece.ky)) + 1;
        this.pieces = initialPieces;
        this.puzzle = puzzle;
        this.listLoops();
        this.hinted = false;
        this.hasMovedEver = false;
        this.unlocked = false;
        this.withdrawn = false;
        this.rot = 0;

        this.polypiece_canvas = document.createElement('CANVAS');
        // size and z-index will be defined later
        puzzle.container.appendChild(this.polypiece_canvas);
        this.polypiece_canvas.classList.add('polypiece');
        this.polypiece_ctx = this.polypiece_canvas.getContext("2d");
    } // PolyPiece

    // -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -   -
    /*
    this method
        - adds pieces of otherPoly to this PolyPiece
        - reorders the pieces inside the polypiece
        - adjusts coordinates of new pieces to make them consistent with this polyPiece
        - re-evaluates the z - index of the polyPieces
    */

    merge(otherPoly, notifyMerge = true) {
        if(this == otherPoly){
            return;
        }

        const changingIndex = Math.max(this.pieces[0].index, otherPoly.pieces[0].index);

        const orgpckxmin = this.pckxmin;
        const orgpckymin = this.pckymin;
        const orgpckxmax = this.pckxmax;
        const orgpckymax = this.pckymax;

        const orgcx = this.x + (this.nx-1) * this.puzzle.scalex / 2;
        const orgcy = this.y + (this.ny-1) * this.puzzle.scaley / 2;

        // remove otherPoly from list of polypieces
        const kOther = this.puzzle.polyPieces.indexOf(otherPoly);
        this.puzzle.polyPieces.splice(kOther, 1);

        // remove other canvas from container
        if (this.puzzle.container.contains(otherPoly.polypiece_canvas)) {
            this.puzzle.container.removeChild(otherPoly.polypiece_canvas);
        } else {
            console.log("The canvas is not a child of the container??", this, otherPoly);
        }

        let forceRedraw = false;
        for (let k = 0; k < otherPoly.pieces.length; ++k) {
            otherPoly.pieces[k].drawn = false;

            if (window.gameplayStarted && notifyMerge) {
                const min = Math.min(this.pieces[0].index, otherPoly.pieces[k].index)
                const max = Math.max(this.pieces[0].index, otherPoly.pieces[k].index)
                // console.log("merge", max, "to", min);

                window.ignore_bounce_pieces.push(min);
                setTimeout(() => {
                    const index = window.ignore_bounce_pieces.indexOf(min);
                    if (index !== -1) {
                        window.ignore_bounce_pieces.splice(index, 1);
                    }
                }, 1000);
                
                change_savedata_datastorage(max, min, true);
                // console.log("done merge", max, "to", min);
            }

            this.pieces.push(otherPoly.pieces[k]);
            // watch leftmost, topmost... pieces
            if (otherPoly.pieces[k].kx < this.pckxmin) {
                this.pckxmin = otherPoly.pieces[k].kx;
                forceRedraw = true;
            }
            if (otherPoly.pieces[k].kx + 1 > this.pckxmax) {
                this.pckxmax = otherPoly.pieces[k].kx + 1;
                forceRedraw = true;
            }
            if (otherPoly.pieces[k].ky < this.pckymin) {
                this.pckymin = otherPoly.pieces[k].ky;
                forceRedraw = true;
            }
            if (otherPoly.pieces[k].ky + 1 > this.pckymax) {
                this.pckymax = otherPoly.pieces[k].ky + 1;
                forceRedraw = true;
            }
            if(this.hinted){
                this.hinted = false;
                // this.polypiece_canvas.classList.remove('hinted');
                forceRedraw = true;
            }
        } // for k

        // sort the pieces by increasing kx, ky

        this.pieces.sort(function (p1, p2) {
            return p1.index - p2.index;
        });

        // redefine consecutive edges
        this.listLoops();

        this.polypiece_drawImage(!forceRedraw);

        const r1 =  -(this.pckxmin - orgpckxmin) * this.puzzle.scalex / 2 - (this.pckxmax - orgpckxmax) * this.puzzle.scalex / 2;
        const r2 =  -(this.pckymin - orgpckymin) * this.puzzle.scaley / 2 - (this.pckymax - orgpckymax) * this.puzzle.scaley / 2;
        const r = rotateVector(r1, r2, -this.rot);

        this.moveTo(
            orgcx - (this.nx-1) * this.puzzle.scalex / 2 - r.x,
            orgcy - (this.ny-1) * this.puzzle.scaley / 2 - r.y
        );
        this.hasMovedEver = true;




        this.puzzle.evaluateZIndex();

        newMerge(changingIndex);

    } // merge

    // -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -   -
    ifNear(otherPoly, ignoreCloseness = false, ignoreRotation = false) {

        if(this.pieces.length > otherPoly.pieces.length){
            return otherPoly.ifNear(this, ignoreCloseness, ignoreRotation)
        }

        if(!ignoreRotation && (this.rot - otherPoly.rot + 360) % 360 > 5) return false;

        let puzzle = this.puzzle;

        // coordinates of origin of full picture for this PolyPieces
        let rotated = rotateVector(this.x + this.nx * puzzle.scalex / 2, this.y + this.ny * puzzle.scaley / 2, this.rot);
        let pprotated = rotateVector(otherPoly.x + otherPoly.nx * puzzle.scalex / 2, otherPoly.y + otherPoly.ny * puzzle.scaley / 2, otherPoly.rot);


        let x = rotated.x - puzzle.scalex * (this.pckxmax + this.pckxmin) / 2;
        let y = rotated.y - puzzle.scaley * (this.pckymax + this.pckymin) / 2;

        let ppx = pprotated.x - puzzle.scalex * (otherPoly.pckxmax + otherPoly.pckxmin) / 2;
        let ppy = pprotated.y - puzzle.scaley * (otherPoly.pckymax + otherPoly.pckymin) / 2;


        if(!ignoreCloseness){
            if (((x - ppx)**2 + (y - ppy)**2) >= puzzle.dConnect) return false; // not close enough
        }

        // this and otherPoly are in good relative position, have they a common side ?
        let neighs = [];
        if (window.pieceSides == 6) {
            for (let k = this.pieces.length - 1; k >= 0; --k) {
                let p1 = this.pieces[k].index;
                let col = (p1 % apnx === 0) ? apnx : (p1 % apnx);
                neighs.push(p1 + apnx);
                neighs.push(p1 - apnx);
                if (col != 1){
                    if(col % 2 == 1) { // note starts at 1 so not the % you would expect
                        neighs.push(p1 - 1 - apnx);
                    }else{
                        neighs.push(p1 - 1 + apnx);
                    }
                    neighs.push(p1 - 1);
                }
                if (col != apnx){
                    if( col % 2 == 1) {
                        neighs.push(p1 + 1 - apnx);
                    }else{
                        neighs.push(p1 + 1 + apnx);
                    }
                    neighs.push(p1 + 1);
                }
            }
        }else{
            for (let k = this.pieces.length - 1; k >= 0; --k) {
                let p1 = this.pieces[k].index;
                neighs.push(p1 + apnx);
                neighs.push(p1 - apnx);
                if (p1 % apnx != 1) neighs.push(p1 - 1);
                if (p1 % apnx != 0) neighs.push(p1 + 1);
            }
        }

        neighs = neighs.filter(n => n >= 0);
        
        if (neighs.some(neigh => otherPoly.pieces.some(piece => piece.index === neigh))) {
            return true;
        }

        // nothing matches

        return false;

    } // ifNear

    // -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -

    /* algorithm to determine the boundary of a PolyPiece
    input : a table of cells, hopefully defining a 'good' PolyPiece, i.e. all connected together
    every cell is given as an object {kx: indice, ky: indice} representing an element of a 2D array.

    returned value : table of Loops, because the boundary may be made of several
    simple loops : there may be a 'hole' in a PolyPiece
    every loop is a list of consecutive edges,
    every edge if an object {kp: index, edge: b} where kp is the index of the cell ine
    the input array, and edge the side (0(top), 1(right), 2(bottom), 3(left))
    every edge contains kx and ky too, normally not used here

    This method does not depend on the fact that pieces have been scaled or not.
    */

    listLoops() {
        // internal : checks if an edge given by kx, ky is common with another cell
        // returns true or false
        const that = this;
        function edgeIsCommon(kx, ky, edge) {
            let ogkx = kx; // original kx
            let ogky = ky; // original ky
            let k;
            if(window.pieceSides == 6) {
                switch (edge) {
                    case 0: ky--; break; // top edge
                    case 1:  // top-right edge
                        if(kx % 2 == 0) {
                            kx++;
                            ky-=1/2;
                        } else {
                            kx++;
                            ky-=1/2;
                        }
                        break;
                    
                    case 2: // bottom-left edge
                        if(kx % 2 == 0) {
                            kx++;
                            ky+=1/2;
                        } else {
                            kx++;
                            ky+=1/2;
                        }
                        break;
                    case 3: ky++; break; // left edge
                    case 4: // bottom-left edge
                        if(kx % 2 == 0) {
                            kx--;
                            ky+=1/2;
                        } else {
                            kx--;
                            ky+=1/2;
                        }
                        break;
                    case 5: // top-left edge
                        if(kx % 2 == 0) {
                            kx--;
                            ky-=1/2;
                        } else {
                            kx--;
                            ky-=1/2;
                        }
                } // switch
            } else {
                switch (edge) {
                    case 0: ky--; break; // top edge
                    case 1: kx++; break; // right edge
                    case 2: ky++; break; // bottom edge
                    case 3: kx--; break; // left edge
                } // switch
            }
            // console.log("final", kx, ky);
            for (k = 0; k < that.pieces.length; k++) {
                if (kx == that.pieces[k].kx && ky == that.pieces[k].ky) {
                    return true; // we found the neighbor
                }
            }
            return false; // not a common edge
        } // function edgeIsCommon

        // -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
        // internal : checks if an edge given by kx, ky is in tbEdges
        // return index in tbEdges, or false

        function edgeIsInTbEdges(kx, ky, edge) {
            let k;
            for (k = 0; k < tbEdges.length; k++) {
                if (kx == tbEdges[k].kx && ky == tbEdges[k].ky && edge == tbEdges[k].edge) return k; // found it
            }
            return false; // not found
        } // function edgeIsInTbEdges

        // -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -

        let tbLoops = []; // for the result
        let tbEdges = []; // set of edges which are not shared by 2 pieces of input
        let k;
        let kEdge;
        let lp; // for loop during its creation
        let currEdge; // current edge
        let tries; // tries counter
        let edgeNumber; // number of edge found during research
        let potNext;

        // table of tries

        let tbTries;
        if(window.pieceSides == 6) {
            tbTries = [
                // kx % 2 == 0 (even columns shifted DOWN)
                [
                    [ { dkx: 0, dky: 0, edge: 1 }, { dkx: +1, dky: -1/2, edge: 5 } ], // edge 0
                    [ { dkx: 0, dky: 0, edge: 2 }, { dkx: +1, dky: 1/2, edge: 0 } ], // edge 1
                    [ { dkx: 0, dky: 0, edge: 3 }, { dkx: 0, dky: +1, edge: 1 } ],  // edge 2
                    [ { dkx: 0, dky: 0, edge: 4 }, { dkx: -1, dky: 1/2, edge: 2 } ],  // edge 3
                    [ { dkx: 0, dky: 0, edge: 5 }, { dkx: -1, dky: -1/2, edge: 3 } ],  // edge 4
                    [ { dkx: 0, dky: 0, edge: 0 }, { dkx: 0, dky: -1, edge: 4 } ], // edge 5
                ],
                // kx % 2 == 1 (odd columns shifted UP)
                [
                    [ { dkx: 0, dky: 0, edge: 1 }, { dkx: +1, dky: -1/2, edge: 5 } ], // edge 0
                    [ { dkx: 0, dky: 0, edge: 2 }, { dkx: +1, dky: +1/2, edge: 0 } ], // edge 1
                    [ { dkx: 0, dky: 0, edge: 3 }, { dkx: 0, dky: +1, edge: 1 } ], // edge 2
                    [ { dkx: 0, dky: 0, edge: 4 }, { dkx: -1, dky: 1/2, edge: 2 } ], // edge 3
                    [ { dkx: 0, dky: 0, edge: 5 }, { dkx: -1, dky: -1/2, edge: 3 } ], // edge 4 
                    [ { dkx: 0, dky: 0, edge: 0 }, { dkx: 0, dky: -1, edge: 4 } ], // edge 5
                ]
            ];
        }else{
            tbTries = [[
                // if we are on edge 0 (top)
                [
                    { dkx: 0, dky: 0, edge: 1 }, // try # 0
                    { dkx: 1, dky: 0, edge: 0 }, // try # 1
                    { dkx: 1, dky: -1, edge: 3 } // try # 2
                ],
                // if we are on edge 1 (right)
                [
                    { dkx: 0, dky: 0, edge: 2 },
                    { dkx: 0, dky: 1, edge: 1 },
                    { dkx: 1, dky: 1, edge: 0 }
                ],
                // if we are on edge 2 (bottom)
                [
                    { dkx: 0, dky: 0, edge: 3 },
                    { dkx: - 1, dky: 0, edge: 2 },
                    { dkx: - 1, dky: 1, edge: 1 }
                ],
                // if we are on edge 3 (left)
                [
                    { dkx: 0, dky: 0, edge: 0 },
                    { dkx: 0, dky: - 1, edge: 3 },
                    { dkx: - 1, dky: - 1, edge: 2 }
                ],
            ]];
        }

        // create list of not shared edges (=> belong to boundary)
        for (k = 0; k < this.pieces.length; k++) {
            for (kEdge = 0; kEdge < (window.pieceSides); kEdge++) {
                if (!edgeIsCommon(this.pieces[k].kx, this.pieces[k].ky, kEdge)){
                    tbEdges.push({ kx: this.pieces[k].kx, ky: this.pieces[k].ky, edge: kEdge, kp: k });
                }
            } // for kEdge
        } // for k

        let loopcount = 0;
        while (tbEdges.length > 0) {
            loopcount++;
            if(loopcount > 1){
                console.log("PANIC!")
            }
            lp = []; // new loop
            currEdge = tbEdges[0];   // we begin with first available edge
            lp.push(currEdge);       // add it to loop
            tbEdges.splice(0, 1);    // remove from list of available sides
            do {
                let parity = 0;
                if(window.pieceSides == 6){
                    if (currEdge.kx % 2 == 1) {
                        parity = 1;
                    }
                }
                let toTry = tbTries[parity][currEdge.edge]; // possible next edges
                for (tries = 0; tries < toTry.length; tries++) {
                    potNext = toTry[tries];
                    edgeNumber = edgeIsInTbEdges(currEdge.kx + potNext.dkx, currEdge.ky + potNext.dky, potNext.edge);
                    
                    if (edgeNumber === false) continue; // can't here
                    // new element in loop
                    currEdge = tbEdges[edgeNumber];     // new current edge
                    lp.push(currEdge);              // add it to loop
                    tbEdges.splice(edgeNumber, 1);  // remove from list of available sides
                    
                    break; // stop tries !
                } // for tries
                if (edgeNumber === false) break; // loop is closed
            } while (1); // do-while exited by break
            tbLoops.push(lp); // add this loop to loops list
        } // while tbEdges...

        // replace components of loops by actual pieces sides
        this.tbLoops = tbLoops.map(loop => loop.map(edge => {
            let cell = this.pieces[edge.kp];
            return cell.sides[edge.edge];
        }));
    } // polyPiece.listLoops

    // -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -   -

    drawPath(ctx, shiftx, shifty) {

        //    ctx.beginPath(); No, not for Path2D

        this.tbLoops.forEach(loop => {
            let without = false;
            loop.forEach(side => {
                side.drawPath(ctx, shiftx, shifty, without);
                without = true;
            });
            ctx.closePath();
        });

    } // PolyPiece.drawPath

    // -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -   -

    polypiece_drawImage(ignoreRedraw) {

        /* resizes canvas to be bigger than if pieces were perfect rectangles
        so that their shapes actually fit in the canvas
        copies the relevant part of gamePicture clipped by path
        adds shadow and emboss
        */
        //       if (this.pieces[0].kx!=1 ||this.pieces[0].ky!= 1) return;
        puzzle = this.puzzle;
        this.nx = this.pckxmax - this.pckxmin + 1;
        this.ny = this.pckymax - this.pckymin + 1;

        if(!ignoreRedraw){
            this.polypiece_canvas.width = this.nx * puzzle.scalex;  // make canvas big enough to fit all pieces
            this.polypiece_canvas.height = this.ny * puzzle.scaley;
        }
        

        // difference between position in this canvas and position in gameImage

        this.offsx = (this.pckxmin - 0.5) * puzzle.scalex;
        this.offsy = (this.pckymin - 0.5) * puzzle.scaley;

        this.path = new Path2D();
        this.drawPath(this.path, -this.offsx, -this.offsy);

        // console.log("tbLoops", this.pieces.length, this.tbLoops);

        let srcx = this.pckxmin ? ((this.pckxmin - 0.5) * puzzle.scalex) : 0;
        let srcy = this.pckymin ? ((this.pckymin - 0.5) * puzzle.scaley) : 0;

        let destx = ( (this.pckxmin ? 0 : 1 / 2) ) * puzzle.scalex;
        let desty = ( (this.pckymin ? 0 : 1 / 2) ) * puzzle.scaley;

        // console.log(this, puzzle)
        
        if(this.pieces[0].index < 0){
            if(apnx > 1){
                if(this.pckxmin == 0){
                    srcx += puzzle.scalex * (1+(this.pckymin)%2) / 3;
                } else { // if(this.pckxmin == this.apnx - 1){            
                    srcx -= puzzle.scalex * (1+(this.pckymin)%2) / 3;
                }
            }
            if(apny > 1){
                if(this.pckymin == 0){
                    srcy += puzzle.scaley * (1+(this.pckxmin)%2) / 3;
                } else { // if(this.pckymin == this.apny - 1)
                    srcy -= puzzle.scaley * (1+(this.pckxmin)%2) / 3;
                }
            }
        }

        let w = puzzle.scalex * (1 + this.pckxmax - this.pckxmin);
        let h = puzzle.scaley * (1 + this.pckymax - this.pckymin);

        // Create an offscreen canvas the size of your destination draw area
        if(!this.maskCanvas){
            this.maskCanvas = document.createElement("canvas");
        }
        this.maskCanvas.width = w;
        this.maskCanvas.height = h;
        const maskCtx = this.maskCanvas.getContext("2d");

        // 1. Draw your puzzle piece shape onto the mask canvas
        maskCtx.save();
        maskCtx.translate(-destx, -desty); // Align the path correctly relative to mask
        maskCtx.fill(this.path);
        maskCtx.restore();

        // 2. Set composite mode to keep only pixels inside the shape
        maskCtx.globalCompositeOperation = "source-in";

        // console.log(w, h, offsetw, offseth);
        // 3. Draw the source image (only visible inside the shape now)
        maskCtx.drawImage(puzzle.gameCanvas, srcx, srcy, w, h, 0,0, w, h);

        // 4. Draw the final result onto your main canvas
        this.polypiece_ctx.drawImage(this.maskCanvas, destx, desty);


        let borders = apnx * apny < 150 && (bevel_size > 0 || shadow_size > 0);

        if(borders){
        
            this.pieces.forEach((pp, kk) => {

                if(true) { //!pp.drawn || !ignoreRedraw
                    this.polypiece_ctx.save();

                    const path = new Path2D();
                    const shiftx = -this.offsx;
                    const shifty = -this.offsy;
                    pp.sides.forEach((side, i) => {
                        if (i == 0) {
                            side.drawPath(path, shiftx, shifty, false);
                        } else {
                            side.drawPath(path, shiftx, shifty, true);
                        }
                    });
                    path.closePath();

                    this.polypiece_ctx.clip(path);
                    
                    let embth = puzzle.scalex * 0.01 * bevel_size * window.scaleFactor * window.additional_zoom;
                    // if(this.hinted){
                    //     embth = puzzle.scalex * 0.01 * window.scaleFactor * window.additional_zoom;
                    // }
                    

                    this.polypiece_ctx.translate(embth / 2, -embth / 2);
                    this.polypiece_ctx.lineWidth = embth;
                    this.polypiece_ctx.strokeStyle = "rgba(0, 0, 0, 0.35)";
                    // if(this.hinted){
                    //     this.polypiece_ctx.strokeStyle = "rgba(250, 0, 0, 1)";
                    // }
                    this.polypiece_ctx.stroke(path);

                    this.polypiece_ctx.translate(-embth, embth);
                    this.polypiece_ctx.strokeStyle = "rgba(255, 255, 255, 0.35)";
                    
                    // if(this.hinted){
                    //     this.polypiece_ctx.strokeStyle = "rgba(250, 0, 0, 1)";
                    // }
                    this.polypiece_ctx.stroke(path);
                    
                    this.polypiece_ctx.restore();

                    pp.drawn = true;
                }
            });
        }

        
        
        // Draw a red outline
        if(this.hinted){
            this.polypiece_ctx.strokeStyle = hint_color;
            this.polypiece_ctx.lineWidth = Math.max(.03 * puzzle.scalex, 7);
            this.polypiece_ctx.stroke(this.path);
        }


    } // PolyPiece.polypiece_drawImage


    moveTo(x, y) {
        // sets the left, top properties (relative to container) of this.canvas
        this.x = x;
        this.y = y;
        this.polypiece_canvas.style.left = (this.x) + 'px';
        this.polypiece_canvas.style.top = (this.y) + 'px';
    } //

    moveAwayFromBorder(){
        const cx = this.x + (this.nx) * this.puzzle.scalex / 2;
        const cy = this.y + (this.ny) * this.puzzle.scaley / 2;

        let len = (this.nx) * this.puzzle.scalex / 2 - this.puzzle.scalex;
        let wid = (this.ny) * this.puzzle.scaley / 2 - this.puzzle.scaley;
        if(this.rot == 1 || this.rot == 3){
            len = (this.ny) * this.puzzle.scaley / 2 - this.puzzle.scaley;
            wid = (this.nx) * this.puzzle.scalex / 2 - this.puzzle.scalex;
        }

        let dx = 0
        if(cx - len < 0){
            dx = cx - len;
        }
        if(cx + len > this.puzzle.contWidth){
            dx = cx + len - this.puzzle.contWidth;
        }
        let dy = 0
        if(cy - wid < 0){
            dy = cy - wid;
        }
        if(cy + wid > this.puzzle.contHeight){
            dy = cy + wid - this.puzzle.contHeight;
        }

        if(dx!=0 || dy!=0){
            this.moveTo(this.x - dx, this.y - dy);
        }
    }

    rotateTo(rot){
        this.rotate(null, rot - this.rot);
    }

    rotate(moving, increase = 1) {
        if(window.rotations == 0) return;
        let num_rots = Math.round(360 / window.rotations);
        if(window.rotations == 180){
            num_rots = 4;
        }
        this.rot = ((this.rot + increase + num_rots) % num_rots) | 0;
        const currentTransform = this.polypiece_canvas.style.transform.replace(/rotate\([-\d.]+deg\)/, '');
        let rotamount = window.rotations;
        if(window.rotations == 180){
            rotamount = 90;
        }
        this.polypiece_canvas.style.transform = `${currentTransform} rotate(${this.rot * rotamount}deg)`;

        if(moving){
            // Adjust position to ensure the piece stays under the cursor
            const centerX = this.x + (this.polypiece_canvas.width / 2);
            const centerY = this.y + (this.polypiece_canvas.height / 2);

            const offsetX = moving.xMouse - centerX;
            const offsetY = moving.yMouse - centerY;

            let { x: changeX, y: changeY } = rotateVector(offsetX, offsetY, -increase);
            changeX = offsetX - changeX;
            changeY = offsetY - changeY;

            moving.ppXInit += changeX;
            moving.ppYInit += changeY;

            this.x = this.x + changeX;
            this.y = this.y + changeY;

            this.moveTo(this.x, this.y);
            this.moveAwayFromBorder();
        }
    }

} // class PolyPiece


//-----------------------------------------------------------------------------
class Puzzle {
    /*
        params contains :

    container : mandatory - given by id (string) or element
                it will not be resized in this script

    ONLY ONE Puzzle object should be instanced.
        only "container is mandatory, nbPieces and pictures may be provided to get
        initial default values.
        Once a puzzle is solved (and event if not solved) another game can be played
        by changing the image file or the number of pieces, NOT by invoking new Puzzle
    */

    constructor(params) {

        this.container = (typeof params.container == "string") ?
            document.getElementById(params.container) :
            params.container;

        /* the following code will add the event Handlers several times if
            new Puzzle objects are created with same container.
            the presence of previous event listeners is NOT detectable
        */
        this.container.addEventListener("mousedown", event => {
            event.preventDefault();
            events.push({ event: 'touch', button: event.button, position: this.relativeMouseCoordinates(event) });

        });
        this.container.addEventListener("contextmenu", event => {
            event.preventDefault();
        });
        this.container.addEventListener("touchstart", event => {
            event.preventDefault();
            if(event.touches.length == 2) {
                rotateCurrentPiece(); return;
            }
            if (event.touches.length != 1) return;
            let ev = event.touches[0];
            events.push({ event: 'touch', button: 0, position: this.relativeMouseCoordinates(ev) });
        }, { passive: false });

        this.container.addEventListener("mouseup", event => {
            event.preventDefault();
            handleLeave();
        });

        this.container.addEventListener("touchend", event => {
            if (event.touches.length == 0) handleLeave();
        });
        this.container.addEventListener("touchleave", event => {
            if (event.touches.length == 0) handleLeave();
        });
        this.container.addEventListener("touchcancel", event => {
            if (event.touches.length == 0) handleLeave();
        });

        this.container.addEventListener("mousemove", event => {
            event.preventDefault();
            // do not accumulate move events in events queue - keep only current one
            if (events.length && events[events.length - 1].event == "move") events.pop();
            
            events.push({ event: 'move', button: event.button, position: this.relativeMouseCoordinates(event) })
        });
        this.container.addEventListener("touchmove", event => {
            event.preventDefault();
            if (event.touches.length != 1) return;
            let ev = event.touches[0];
            // do not accumulate move events in events queue - keep only current one
            if (events.length && events[events.length - 1].event == "move") events.pop();
            // console.log("touch", event.offsetX, event.offsetY, event)
            events.push({ event: 'move', button: 0, position: this.relativeMouseCoordinates(ev) });
        }, { passive: false });

        /* create canvas to contain picture - will be styled later */
        this.gameCanvas = document.createElement('CANVAS');
        this.container.appendChild(this.gameCanvas)

        this.srcImage = new Image();
        this.imageLoaded = false;
        this.srcImage.addEventListener("load", () => imageLoaded(this));

        function handleLeave() {
            // console.log("HANDLING LEAVE")
            events.push({ event: 'leave' }); //
        }

        this.scale_zoom = 1;

    } // Puzzle

    //- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    getContainerSize() {
        let styl = window.getComputedStyle(this.container);

        /* dimensions of container */
        this.contWidth = parseFloat(styl.width);
        this.contHeight = parseFloat(styl.height);
        
    }

    //- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    puzzle_create(coordinates, groups, hasmoved, unlocked) {
        console.log(coordinates, groups, hasmoved, unlocked)

        // Set the seed of Math.random to window.apseed
        if(window.apseed){
            console.log(window.apseed)
            if (typeof window.apseed !== 'number' || !Number.isInteger(window.apseed)) {
                const hash = Array.from(String(window.apseed)).reduce((acc, char) => {
                    return acc * 31 + char.charCodeAt(0);
                }, 0);
                console.log(hash)
                setRandomSeed((hash + window.slot) % 10000);
            } else {
                setRandomSeed((window.apseed + window.slot) % 10000);
            }
        }

        this.container.innerHTML = ""; // forget contents

        /* define the number of rows / columns to have almost square pieces
            and a total number as close as possible to the requested number
        */
        this.getContainerSize();
        this.computenxAndny(apnx, apny);
        /* assuming the width of pieces is 1, computes their height
                (computenxAndny aims at making relativeHeight as close as possible to 1)
        */
        this.relativeHeight = (this.srcImage.naturalHeight / this.ny) / (this.srcImage.naturalWidth / this.nx);

        this.defineShapes({ coeffDecentr: 0.12, twistf: [twist0, twist1, twist2, twist3, twist3, null][document.getElementById("shape").value - 1] });

        this.polyPieces = [];

        if(coordinates.length != groups.length){
            console.log("coordinates and groups do not have the same length?", coordinates, groups)
        }

        for (let key in coordinates) {
            let pieces_in_group = [];
            for (let ind of groups[key]) {
                let w = (ind-1) % window.apnx;
                let h = Math.floor((ind-1) / window.apnx);
                
                if(ind < 0){
                    w = -ind;
                    h = -1;
                }
                if(this.pieces[h][w]){
                    pieces_in_group.push(this.pieces[h][w]);
                    if(ind != key){
                        newMerge(ind, false);
                    }
                }
            }
            if(pieces_in_group.length > 0) {
                let ppp = new PolyPiece(pieces_in_group, this);
                ppp.hasMovedEver = hasmoved[key];
                ppp.unlocked = unlocked[key];
                ppp.moveTo(
                    coordinates[key][0] * puzzle.contWidth, 
                    coordinates[key][1] * puzzle.contHeight
                )
                if(coordinates[key][2]){
                    ppp.rotate(null, coordinates[key][2]);
                }
                this.polyPieces.push(ppp);
            }
        }

        this.evaluateZIndex();

        console.log("done evaluate z index")
    } // Puzzle.create

    //- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    /* computes the number of lines and columns of the puzzle,
    finding the best compromise between the requested number of pieces
    and a square shap for pieces
    result in this.nx and this.ny;
    */

    computenxAndny(inx = -1, iny = -1) {

        if(inx > 0){
            this.nx = inx;
            this.ny = iny;
            return;
        }

        let kx, ky, width = this.srcImage.naturalWidth, height = this.srcImage.naturalHeight, npieces = this.nbPieces;
        let err, errmin = 1e9;
        let ncv, nch;


        let nHPieces = mround(msqrt(npieces * width / height));
        let nVPieces = mround(npieces / nHPieces);
        
        /* based on the above estimation, we will try up to + / - 2 values
            and evaluate (arbitrary) quality criterion to keep best result
        */

        for (ky = 0; ky < 5; ky++) {
            ncv = nVPieces + ky - 2;
            for (kx = 0; kx < 5; kx++) {
            nch = nHPieces + kx - 2;
            err = nch * height / ncv / width;
            err = (err + 1 / err) - 2; // error on pieces dimensions ratio)
            err += mabs(1 - nch * ncv / npieces); // adds error on number of pieces

            if (err < errmin) { // keep smallest error
                errmin = err;
                this.nx = nch;
                this.ny = ncv;
            }
            } // for kx
        } // for ky

    } // computenxAndny

    //- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    defineShapes(shapeDesc) {
        // define shapes as if the width and height of a piece were 1

        /* first, place the corners of the pieces
            at some distance of their theoretical position, except for edges
        */
        let np;

        if(window.pieceSides == 6){
            this.corners_and_sides_6(shapeDesc);
        }else{
            this.corners_and_sides_4(shapeDesc);
        }

        if(window.fake_pieces_mimic.length >= 1){
            this.pieces[-1] = [];

            for(let i = 0; i < window.fake_pieces_mimic.length; i++){
                let mimic_piece_x = (window.fake_pieces_mimic[i]-1) % this.nx;
                let mimic_piece_y = Math.floor((window.fake_pieces_mimic[i]-1) / this.nx);

                this.pieces[-1][i+1] = np = new Piece(mimic_piece_x, mimic_piece_y, -i - 1);

                for (let sideIndex = 0; sideIndex < this.pieces[mimic_piece_y][mimic_piece_x].sides.length; sideIndex++) {
                    np.sides[sideIndex] = this.pieces[mimic_piece_y][mimic_piece_x].sides[sideIndex];
                }

            }
        }

    } // Puzzle.defineShapes

    corners_and_sides_4(shapeDesc) {

        let { coeffDecentr, twistf } = shapeDesc;
        const corners = [];
        const nx = this.nx, ny = this.ny;
        let np;

        for (let ky = -1; ky <= ny+1; ++ky) {
            corners[ky] = [];
            for (let kx = -1; kx <= nx+1; ++kx) {
                // Randomize coeffDecentr between 0 and 0.5 for each piece
                if(document.getElementById("shape").value == 6){
                    coeffDecentr = randomIn(ky * nx + kx + 1 + 1) * .5;
                }
                if(document.getElementById("shape").value == 5){
                    coeffDecentr = 0;
                }
                corners[ky][kx] = new Point(kx + alea(-coeffDecentr, coeffDecentr),
                    ky + alea(-coeffDecentr, coeffDecentr));
                if (kx <= 0) corners[ky][kx].x = 0;
                if (kx >= nx) corners[ky][kx].x = nx;
                if (ky <= 0) corners[ky][kx].y = 0;
                if (ky >= ny) corners[ky][kx].y = ny;
            } // for kx
        } // for ky

        // Array of pieces
        this.pieces = [];
        for (let ky = 0; ky < ny; ++ky) {
            this.pieces[ky] = [];
            for (let kx = 0; kx < nx; ++kx) {
                // Randomly select a twist function for this piece
                if(document.getElementById("shape").value == 6){
                    let twistFunctions = [twist0, twist1, twist2, twist3];
                    twistf = twistFunctions[Math.floor(randomIn(ky * nx + kx + 1) * twistFunctions.length)];
                }
                this.pieces[ky][kx] = np = new Piece(kx, ky, ky * nx + kx + 1);
                // top side
                if (ky == 0) {
                    np.sides[0].points = [corners[ky][kx], corners[ky][kx + 1]];
                    np.sides[0].type = "d";
                } else {
                    np.sides[0] = this.pieces[ky - 1][kx].sides[2].reversed();
                }
                // right side
                np.sides[1].points = [corners[ky][kx + 1], corners[ky + 1][kx + 1]];
                np.sides[1].type = "d";
                if (kx < nx - 1) {
                    if (intAlea(2)) // randomly twisted on one side of the side
                    twistf(np.sides[1], corners[ky][kx], corners[ky + 1][kx]);
                    else
                    twistf(np.sides[1], corners[ky][kx + 2], corners[ky + 1][kx + 2]);
                }
                // bottom side
                np.sides[2].points = [corners[ky + 1][kx + 1], corners[ky + 1][kx]];
                np.sides[2].type = "d";
                if (ky < ny - 1) {
                    if (intAlea(2)) // randomly twisted on one side of the side
                    twistf(np.sides[2], corners[ky][kx + 1], corners[ky][kx]);
                    else
                    twistf(np.sides[2], corners[ky + 2][kx + 1], corners[ky + 2][kx]);
                }
                // left side
                if (kx == 0) {
                    np.sides[3].points = [corners[ky + 1][kx], corners[ky][kx]];
                    np.sides[3].type = "d";
                } else {
                    np.sides[3] = this.pieces[ky][kx - 1].sides[1].reversed()
                }
            } // for kx
        } // for ky
    }

    
    corners_and_sides_6(shapeDesc) {


        let { coeffDecentr, twistf } = shapeDesc;
        const corners = [];
        const nx = this.nx, ny = this.ny;

        for (let ky = -1; ky <= 2*ny+2; ++ky) {
            corners[ky] = [];
            for (let kx = -1; kx <= nx+2; ++kx) {
                if(document.getElementById("shape").value == 6){
                    coeffDecentr = randomIn(ky * nx + kx + 1 + 1) * .5;
                }
                if(document.getElementById("shape").value == 5){
                    coeffDecentr = 0;
                }
                if(ky % 2 == 0){
                    if(kx % 2 == 0){
                        corners[ky][kx] = new Point(corner_to_shape_dist + kx, ky * 0.5);
                    }else{
                        corners[ky][kx] = new Point(kx, ky * 0.5);
                    }
                }else{
                    if(kx % 2 == 0){
                        corners[ky][kx] = new Point(kx, ky * 0.5);
                    }else{
                        corners[ky][kx] = new Point(kx + corner_to_shape_dist, ky * 0.5);
                    }
                }
                if(ky > 1 && ky < 2*ny && kx > 0 && kx < nx){
                    corners[ky][kx].y += alea(-coeffDecentr, coeffDecentr);
                    corners[ky][kx].x += alea(-coeffDecentr, coeffDecentr);
                }
            }
        }

        let np;

        // Array of pieces
        this.pieces = [];
        for (let ky = 0; ky < ny; ++ky) {
            this.pieces[ky] = [];
        }
        for (let kx = 0; kx < nx; ++kx) {
            for (let ky = 0; ky < ny; ++ky) {
                if(document.getElementById("shape").value == 6){
                    let twistFunctions = [twist0, twist1, twist2, twist3];
                    twistf = twistFunctions[Math.floor(randomIn(ky * nx + kx + 1) * twistFunctions.length)];
                }
                const upy = (kx % 2 == 1) ? 1 : 0; // offset for odd columns

                this.pieces[ky][kx] = np = new Piece(kx, ky + upy/2, ky * nx + kx + 1);


                const idy0 = 2 * ky + upy;
                const idx0 = kx;
                const c0 = corners[idy0][idx0];
                const idy1 = 2 * ky + upy;
                const idx1 = kx + 1;
                const c1 = corners[idy1][idx1];
                const idy2 = 2 * ky + 1 + upy;
                const idx2 = kx + 1;
                const c2 = corners[idy2][idx2];
                const idy3 = 2 * ky + 2 + upy;
                const idx3 = kx + 1;
                const c3 = corners[idy3][idx3];
                const idy4 = 2 * ky + 2 + upy;
                const idx4 = kx;
                const c4 = corners[idy4][idx4];
                const idy5 = 2 * ky + 1 + upy;
                const idx5 = kx;
                const c5 = corners[idy5][idx5];

                // top side
                np.sides[0].points = [c0, c1];
                np.sides[0].type = "d";
                if(ky > 0){
                    np.sides[0] = this.pieces[ky - 1][kx].sides[3].reversed();
                }

                // top-right side, never already exists because y is iterated first
                np.sides[1].points = [c1, c2];
                np.sides[1].type = "d";
                if(kx < nx - 1 && (ky > 0 || kx % 2 == 1)) { // if not last column, and not first row or odd column
                    if (intAlea(2)){
                        twistf(np.sides[1], corners[idy1-1][idx1+1], corners[idy2-1][idx2+1], 0.6);
                    } else {
                        twistf(np.sides[1], corners[idy1+1][idx1-1], corners[idy2+1][idx2-1], 0.6);
                    }
                }

                // bottom-right side, never already exists because y is iterated first
                np.sides[2].points = [c2, c3];
                np.sides[2].type = "d";
                if(kx < nx - 1 && (ky < ny - 1 || kx % 2 == 0)) { // if not last column, and not last row or even column
                    if (intAlea(2)){
                        twistf(np.sides[2], corners[idy2-1][idx2-1], corners[idy3-1][idx3-1], 0.6);
                    } else {
                        twistf(np.sides[2], corners[idy2+1][idx2+1], corners[idy3+1][idx3+1], 0.6);
                    }
                }

                // bottom side
                np.sides[3].points = [c3, c4];
                np.sides[3].type = "d";
                if(ky < ny - 1){
                    if (intAlea(2)){
                        twistf(np.sides[3], corners[idy3-1][idx3], corners[idy4-1][idx4]);
                    } else {
                        twistf(np.sides[3], corners[idy3+1][idx3], corners[idy4+1][idx4]);
                    }   
                }

                // bottom-left side
                np.sides[4].points = [c4, c5];
                np.sides[4].type = "d";
                if (kx > 0 && (ky < ny - 1 || kx % 2 == 0)) { // if not first column, and not last row or even column
                    if (kx % 2 == 0){
                        np.sides[4] = this.pieces[ky][kx - 1].sides[1].reversed();
                    } else {
                        np.sides[4] = this.pieces[ky + 1][kx - 1].sides[1].reversed();
                    }  
                }

                // top-left side
                np.sides[5].points = [c5, c0];
                np.sides[5].type = "d";
                if (kx > 0 && (ky > 0 || kx % 2 == 1)) { // if not first column, and not first row or odd column
                    if(kx % 2 == 0){
                        np.sides[5] = this.pieces[ky - 1][kx - 1].sides[2].reversed();
                    } else {
                        np.sides[5] = this.pieces[ky][kx - 1].sides[2].reversed();
                    }
                }

            } // for kx
        } // for ky
        console.log("pieces defined", this.pieces);
    }



    //- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    puzzle_scale() {

        // we suppose we want the picture to fill 90% on width or height and less or same on other dimension
        // this 90% might be changed and depend on the number of columns / rows.

        // suppose image fits in height
        puzzle.getContainerSize();

        const aspectRatio = this.srcImage.naturalWidth / this.srcImage.naturalHeight;
        if (this.contWidth / this.contHeight > aspectRatio) {
            this.gameHeight = this.contHeight;
            this.gameWidth = this.contHeight * aspectRatio;
        } else {
            this.gameWidth = this.contWidth;
            this.gameHeight = this.contWidth / aspectRatio;
        }

        // this.gameWidth *= 2;
        // this.gameHeight *= 2;


        /* get a scaled copy of the source picture into a canvas */
        this.gameCanvas = document.createElement('CANVAS');
        this.gameCanvas.width = this.gameWidth;
        this.gameCanvas.height = this.gameHeight;
        this.gameCtx = this.gameCanvas.getContext("2d");

        let image_enlarge_x=1, image_enlarge_y=1;
        if(window.pieceSides == 6){
            image_enlarge_x = (this.nx + corner_to_shape_dist) / (this.nx);
            image_enlarge_y = (this.ny + 1/2) / (this.ny);
            image_enlarge_x = mmax(image_enlarge_x, image_enlarge_y);
            image_enlarge_y = image_enlarge_x;
        }



        /* scale pieces */
        this.scalex = window.downsize_to_fit * this.gameWidth / this.nx;    // average width of pieces, add zoom here
        this.scaley = window.downsize_to_fit * this.gameHeight / this.ny;   // average height of pieces
        this.diff_scalex = 0;
        this.diff_scaley = 0;


        if(window.make_pieces_square){
            if(window.pieceSides == 4){
                let newx = mmin(this.scalex, this.scaley);
                let newy = newx;
                this.diff_scalex = this.scalex - newx;
                this.diff_scaley = this.scaley - newy;
                this.scalex = newx;
                this.scaley = newy;
                console.log("made pieces square scalex, scaley", this.scalex, this.scaley);
            }else{
                let newx, newy, mmm;
                if(this.scalex * Math.sqrt(3) < this.scaley * 2){
                    mmm = this.scalex * Math.sqrt(3);
                }else{
                    mmm = this.scaley * Math.sqrt(3);
                }
                newx = mmm / 2;
                newy = mmm / Math.sqrt(3);
                this.diff_scalex = this.scalex - newx;
                this.diff_scaley = this.scaley - newy;
                this.scalex = newx;
                this.scaley = newy;
                console.log("made pieces square scalex, scaley (6)", this.scalex, this.scaley);
            }
        }

        console.log(this.diff_scalex, this.gameWidth * window.downsize_to_fit * image_enlarge_x, this.nx)

        this.gameCtx.drawImage(
            this.srcImage, 
            - this.diff_scalex * this.nx / 2, 
            - this.diff_scaley * this.ny / 2, 
            this.gameWidth * window.downsize_to_fit * image_enlarge_x, 
            this.gameHeight * window.downsize_to_fit * image_enlarge_y
        ); //safe
        

        this.gameCanvas.classList.add("gameCanvas");
        this.gameCanvas.style.zIndex = 100000002;

 
        

        this.pieces.forEach(row => {
            row.forEach(piece => piece.piece_scale(this));
        }); // this.pieces.forEach, safe

        /* calculate offset for centering image in container */
        this.offsx = (this.contWidth - this.gameWidth) / 2;
        this.offsy = (this.contHeight - this.gameHeight) / 2;

        /* computes the distance below which two pieces connect
            depends on the actual size of pieces, with lower limit */
        this.dConnect = 0.85 * mmax(10, mmin(this.scalex, this.scaley) / 10) * window.scaleFactor * window.additional_zoom;
        this.dConnect *= this.dConnect; // square of distance


    } // Puzzle.scale

    //- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    relativeMouseCoordinates(event) {

        /* takes mouse coordinates from mouse event
            returns coordinates relative to container, even if page is scrolled or zoommed */

        const br = this.container.getBoundingClientRect();
        
        return {
            x: (event.clientX - br.x) * window.scaleFactor / window.additional_zoom,
            y: (event.clientY - br.y) * window.scaleFactor / window.additional_zoom,
            p_x: (event.clientX - br.x) / br.width,
            p_y: (event.clientY - br.y) / br.height
        };
    } // Puzzle.relativeMouseCoordinates

    

    evaluateZIndex() {
        // re-assign zIndex
        this.polyPieces.forEach((pp, k) => {
            pp.polypiece_canvas.style.zIndex = -pp.pieces.length * 10000 + k + 100000000;
        });
    } // Puzzle.evaluateZIndex
} // class Puzzle
//-----------------------------------------------------------------------------

let loadFile;
{ // scope for loadFile

    let options;

    let elFile = document.createElement('input');
    elFile.setAttribute('type', 'file');
    elFile.setAttribute('multiple', 'multiple');
    elFile.style.display = 'none';
    elFile.addEventListener("change", getFile);

    function getFile() {
        if (this.files.length == 0) {
            //      returnLoadFile ({fail: 'no file'});
            return;
        }
        
        let reader = new FileReader();
        let randomIndex = Math.floor(Math.random() * this.files.length);

        reader.addEventListener('load', () => {
            setImagePath(reader.result);
        });
        reader.readAsDataURL(this.files[randomIndex]);
    } // getFile

    loadFile = function (ooptions) {
        elFile.setAttribute("accept", "image/*");
        elFile.value = null; // else, re-selecting the same file does not trigger "change"
        elFile.click();
    } // loadFile
} //  // scope for loadFile

var defaultImagePath = "https://images.pexels.com/photos/147411/italy-mountains-dawn-daybreak-147411.jpeg";
var imagePath = "https://images.pexels.com/photos/147411/italy-mountains-dawn-daybreak-147411.jpeg";

function loadInitialFile() {
    setImagePath(window.defaultImagePath);
}

//-----------------------------------------------------------------------------
function imageLoaded(puzzle) {
    events.push({ event: "srcImageLoaded" });
    puzzle.imageLoaded = true;
} // imageLoaded

//-----------------------------------------------------------------------------
function fitImage(img, width, height) {
    /* The image is a child of puzzle.container. It will be styled to be as big as possible, not wider than width,
    not higher than height, centered in puzzle.container
    (width and height must be less than or equal to the container dimensions)
    */

    let wn = img.naturalWidth;
    let hn = img.naturalHeight;
    let w = width;
    let h = w * hn / wn;
    if (h > height) {
    h = height;
    w = h * wn / hn;
    }
    img.style.position = "absolute";
    img.style.width = w + "px";
    img.style.height = h + "px";
    img.style.top = "50%";
    img.style.left = "50%";
    img.style.transform = "translate(-50%,-50%)";
}

//-----------------------------------------------------------------------------
let animate;
let events = []; // queue for events
let gameStarted = false;
window.gameplayStarted = false;
let manually_load_save_file = false;


// Fetch scale factor from CSS
window.scaleFactor = getComputedStyle(document.documentElement).getPropertyValue('--scale-factor').trim();

let tmpImage;
function loadImageFunction(){
    puzzle.container.innerHTML = ""; // forget contents
    tmpImage = document.createElement("img");
    tmpImage.src = puzzle.srcImage.src;
    // console.log(puzzle.srcImage.src)
    puzzle.getContainerSize();
    fitImage(tmpImage, puzzle.contWidth * 0.90, puzzle.contHeight * 0.90);
    
    tmpImage.style.boxShadow = `${0.02 * puzzle.contWidth}px ${0.02 * puzzle.contWidth}px ${0.02 * puzzle.contWidth}px rgba(0, 0, 0, 0.5)`;
    
    puzzle.container.appendChild(tmpImage);
    
    puzzle.prevWidth = puzzle.contWidth;
    puzzle.prevHeight = puzzle.contHeight;
}

let moving; // for information about moved piece
{ // scope for animate
    let state = 0;

    animate = function () {
        requestAnimationFrame(animate);

        let event;
        
        if (events.length) event = events.shift(); // read event from queue
        
        // resize event
        if (event && event.event == "resize") {

            // remember dimensions of container before resize
            puzzle.getContainerSize();
            if (state == 15 || state > 60) { // resize initial or final picture
                fitImage(tmpImage, puzzle.contWidth * window.downsize_to_fit, puzzle.contHeight * window.downsize_to_fit);
            }
            else if (state >= 25) { // resize pieces
                
                const x_change = puzzle.contWidth / puzzle.prevWidth;
                const y_change = puzzle.contHeight / puzzle.prevHeight;

                puzzle.puzzle_scale();
                
                console.log("start scaling pieces")
                puzzle.polyPieces.forEach(pp => {                    
                    let nnx = pp.x;
                    let nny = pp.y;

                    pp.moveTo(nnx, nny);
                    pp.polypiece_drawImage(false);


                    pp.moveTo(pp.x * x_change, pp.y * y_change);

                }); // puzzle.polypieces.forEach
                console.log("end scaling pieces")
            }
            
            puzzle.prevWidth = puzzle.contWidth;
            puzzle.prevHeight = puzzle.contHeight;

            return;
        } // resize event

        if(window.goTo8888State){
            state = 8888;
        }

        switch (state) {
            /* initialisation */
            case 0:
                
                if((window.is_connected || window.play_solo) && window.set_ap_image && window.choose_ap_image){
                    state = 10;
                }else{
                    return;
                }
            break;

            case 10: // load image
                document.getElementById("m4").textContent = "Loading image...";
                loadImageFunction();
                document.getElementById("m4").textContent = "Start";
                state = 15;
                return;


            /* wait for choice of number of pieces */
            case 15:
                if (event && event.event == "srcImageLoaded") {
                    // display centered initial image
                    loadImageFunction();
                    return;
                } 
                
                if ((event && event.event == "nbpieces") || (window.LoginStart && window.is_connected) || (window.start_solo_immediately)) {
                    document.getElementById("m4").textContent = "Loading pieces...";

                    bevel_size = localStorage.getItem("option_bevel_2");
                    if (bevel_size === null) bevel_size = 0.1;

                    shadow_size = localStorage.getItem("option_shadow_2");
                    if (shadow_size === null) shadow_size = 0;

                    state = 17;
                    if(window.is_connected){
                        if(window.apworld == "0.2.0" || window.apworld == "0.3.0"){
                            localStorage.setItem(`image_${window.apseed}_${window.slot}`, imagePath);
                        }else{
                            const dbRequest = indexedDB.open("ImageDatabase", 1);

                            dbRequest.onupgradeneeded = (event) => {
                                const db = event.target.result;
                                if (!db.objectStoreNames.contains("images")) {
                                    db.createObjectStore("images", { keyPath: "id" });
                                }
                            };

                            dbRequest.onsuccess = (event) => {
                                const db = event.target.result;
                                const transaction = db.transaction(["images"], "readwrite");
                                const store = transaction.objectStore("images");
                                const putRequest = store.put({ id: `${window.apseed}_${window.slot}`, imagePath });

                                putRequest.onsuccess = () => {
                                    console.log("Image successfully saved to IndexedDB.");
                                };

                                putRequest.onerror = () => {
                                    console.log("Error saving image to IndexedDB.");
                                };
                            };

                            dbRequest.onerror = () => {
                                console.log("Error opening IndexedDB.");
                            };
                        }
                    }
                }
                
                return;

            
            case 17: // load save!

                if(unlocked_pieces.length == 0){
                    console.log("No unlocked pieces!")
                    return;
                }
                
                state = 18;
                accept_pending_actions = true;

                get_save_data_from_data_storage();

                async function get_save_data_from_data_storage(keys) {
                    window.save_file = {};
                    if(!window.play_solo){
                        let keys = [];
                
                        for (let p = 1; p <= apnx * apny; p++) {
                            keys.push(`JIG_PROG_${window.slot}_${p}`);
                        }
                        if(window.fake_pieces_mimic.length >= 1){
                            for (let p = 1; p <= window.fake_pieces_mimic.length; p++) {
                                keys.push(`JIG_PROG_${window.slot}_${-p}`);
                            }
                        }

                        let client = window.getAPClient();                  

                        await client.storage.notify(keys, (key, value, oldValue) => {
                            console.log("notify", key, value, oldValue);
                            do_action(key, value, oldValue, false);
                        });

                        keys.push(`JIG_PROG_${window.slot}_M`);
                        keys.push(`JIG_PROG_${window.slot}_O`);

                        let results = (await client.storage.fetch(keys, true))
                        console.log("results", results)
                        
                        for (let [key, value] of Object.entries(results)) {
                            let spl = key.split("_")[3];
                            if (spl === "O"){
                                if(!window.ignoreAspectRatio){
                                    console.log("value is", value)
                                    if(value){
                                        if(Math.abs(parseFloat(value) - puzzle.srcImage.width / puzzle.srcImage.height) > 0.05){
                                            alert("Warning, you are not using the same aspect ratio as before. Pieces might not be in the correct relative position. You can refresh now to discard this login (if you do ignore this error next time).")
                                        }
                                    }
                                    console.log("put to ", puzzle.srcImage.width / puzzle.srcImage.height)
                                    change_savedata_datastorage("O", puzzle.srcImage.width / puzzle.srcImage.height, true);
                                }
                            }else{
                                if(value){
                                    if (spl === "M") {
                                        numberOfMergesAtStart = parseInt(value);
                                    }else {
                                        let pp_index = parseInt(spl);
                                        window.save_file[pp_index] = [value, true];
                                    }
                                }
                            }
                            
                        }
                    }

                    let num_rots = Math.round(360 / window.rotations);
                    if (window.rotations == 0) num_rots = 1;

                    unlocked_pieces.sort(() => Math.random() - 0.5).forEach(index => {
                        if (window.save_file[index] === undefined) {
                            let random_rotation = 0;
                            if (window.rotations == 180){
                                random_rotation = Math.floor(2 * Math.floor((index * 2345.1234) % 2));
                            }else{
                                random_rotation = Math.floor(((index+10) * 2345.1234) % num_rots);
                            }
                            window.save_file[index] = 
                            [
                                [
                                    ((index+1000) * 4321.1234) % 0.10, 
                                    ((index+1000) * 1234.4321) % 0.5, 
                                    random_rotation
                                ], false
                            ];
                        }
                    });

                    unlocked_fake_pieces.sort(() => Math.random() - 0.5).forEach(index => {
                        if (window.save_file[index] === undefined) {
                            let random_rotation = 0;
                            if (window.rotations == 180){
                                random_rotation = Math.floor(2 * Math.floor(((index+10) * 2345.1234) % 2));
                            }else{
                                random_rotation = Math.floor(((index+10) * 2345.1234) % num_rots);
                            }
                            window.save_file[index] = 
                            [
                                [
                                    ((index+1000) * 4321.1234) % 0.10, 
                                    ((index+1000) * 1234.4321) % 0.5, 
                                    random_rotation
                                ], false
                            ];
                        }
                    });
                    
                    state = 19;
                }
            case 18: // wait for save file
                return;

            // case 18.5:
            //     console.log("waiting 10 seconds")
            //     setTimeout(() => {
            //         state = 19;
            //     }, 10000);
            //     state = 18.7;
            //     return;
            // case 18.7:
            //     return;



            case 19:  // process save file and start game
                let coordinates = {}
                let groups = {}
                let hasmoved = {}
                let unlocked = {}

                let all_indices = []

                for (let key = 1; key <= window.apnx * window.apny; key++) {
                    all_indices.push(key);
                }
                if(window.fake_pieces_mimic.length >= 1){
                    for(let i = 0; i < window.fake_pieces_mimic.length; i++){
                        all_indices.push(-1 - i);
                    }
                }

                for (let [key, value] of Object.entries(window.save_file)) {
                    all_indices = all_indices.filter(index => index !== parseInt(key));

                    if (Array.isArray(value[0])) {
                        coordinates[key] = value[0];
                        hasmoved[key] = value[1];
                        groups[key] = [parseInt(key)];
                        unlocked[key] = true;
                    } else {
                        let refer_to = value[0];
                        let groupKey = Object.keys(groups).find(groupKey => groups[groupKey].includes(refer_to));
                        // console.log(key, refer_to)
                        if (groupKey) {
                            groups[groupKey].push(parseInt(key));
                        } else {
                            console.log(key, refer_to, "not found, gonna go ahead and put it at 0,0")
                            coordinates[key] = [0,0];
                            groups[key] = [parseInt(key)];
                            unlocked[key] = true;
                        }
                    }
                }

                for(let key of all_indices){
                    groups[key] = [key];
                    coordinates[key] = [30,30];
                    hasmoved[key] = false;
                    unlocked[key] = false;
                }

                console.log("STARTING GAME")
                gameStarted = true;
                menu.open();

                document.getElementById("m1").style.display = "none";
                document.getElementById("m2").style.display = "none";
                document.getElementById("m3").style.display = "none";
                document.getElementById("m4").style.display = "none";
                document.getElementById("m5").style.display = "none";
                document.getElementById("m10b").style.display = "none";
                document.getElementById("o1a").style.display = "none";
                document.getElementById("o1b").style.display = "none";

                /* prepare puzzle */
                puzzle.puzzle_create(coordinates, groups, hasmoved, unlocked); // create shape of pieces, independant of size



                puzzle_ini = true;

                console.log("done getting backlog of actions")
                
                puzzle.puzzle_scale();

                for (let pp of puzzle.polyPieces) {
                    if (!pp.hasMovedEver) {
                        const newppx = pp.x - puzzle.scalex / 2;
                        const newppy = pp.y - puzzle.scaley / 2;
                        pp.moveTo(newppx, newppy);
                    }
                }

                console.log("done scaling puzzle")
                puzzle.polyPieces.forEach(pp => {
                    pp.polypiece_drawImage(false);
                }); // puzzle.polypieces.forEach
                console.log("drawn each piece")
                puzzle.gameCanvas.style.top = puzzle.offsy + "px";
                puzzle.gameCanvas.style.left = puzzle.offsx + "px";
                puzzle.gameCanvas.style.display = "block";

                window.save_loaded = true;

                console.log("pending actions:", pending_actions)

                process_pending_actions = true;
                accept_pending_actions = false;

                try {
                    for(let data of pending_actions){
                        console.log("Pending action", data, pending_actions)
                        do_action(data[0], data[1], data[2], false);
                    }
                } catch (error) {
                    console.error("Error processing pending actions:", error);
                    alert("Error while loading, please refresh the page (and I would appreciate a ping via discord with a screenshot of the debug panel (F12))")
                }

                console.log("DONE WITH INI!", puzzle)

                state = 25;
                break;


            case 25: // spread pieces
                puzzle.gameCanvas.style.display = "none"; // hide reference image
                
                state = 40;
                break;

            case 40: // evaluate z index
                
                puzzle.polyPieces.sort((a, b) => Math.random() - 0.5);
                puzzle.evaluateZIndex();
                state = 45;

                break;

            case 45:
                // run function after ini
                state = 50;
                
                window.gameplayStarted = true;            
                break;

                /* wait for user grabbing a piece or other action */
            case 50:
                if (!event) return;

                if (!window.is_connected && !window.play_solo) return;

                if (event.event == "leave") {
                    moving = null;
                }
                
                if (event.event != "touch") return;

                console.log(event)
                if(event.button == 0){
                    const event_x = event.position.x;
                    const event_y = event.position.y;
                    // console.log(event_x, event_y)
    
                    moving = {
                        xMouseInit: event_x,
                        yMouseInit: event_y,
                        xMouse: event_x,
                        yMouse: event_y
                    }
    
                    /* evaluates if contact inside a PolyPiece, by decreasing z-index */
                    puzzle.polyPieces.sort((a, b) => a.polypiece_canvas.style.zIndex - b.polypiece_canvas.style.zIndex);
                    for (let k = puzzle.polyPieces.length-1; k >= 0; k--) {
                        let pp = puzzle.polyPieces[k];
                        
                        const cx = pp.x + pp.nx * puzzle.scalex / 2;
                        const cy = pp.y + pp.ny * puzzle.scaley / 2;
                        
                        const roxy = rotateVector(event_x - cx, event_y - cy, pp.rot);
    
                        if (pp.polypiece_ctx.isPointInPath(pp.path, cx + roxy.x - pp.x, cy + roxy.y - pp.y)) { // event_x - pp.x, event_y - pp.y
                            moving.pp = pp;
                            moving.ppXInit = pp.x;
                            moving.ppYInit = pp.y;
                            // move selected piece to top of polypieces stack
                            puzzle.polyPieces.splice(k, 1);
                            puzzle.polyPieces.push(pp);
                            pp.polypiece_canvas.style.zIndex = 100000001; // to foreground
                            
                            state = 55;
                            return;
                        }
                    } // for k
                }

                if(zoomP == 1) return;

                startDragX = event.position.p_x;
                startDragY = event.position.p_y;

                state = 52;
                break;

            case 52:  //dragging screen
                if (!event) return;
                switch (event.event) {
                    case "move":
                        // console.log(event.position.p_x, startDragX, zoomX)
                        zoomX += (event.position.p_x - startDragX) * zoomP;
                        zoomY += (event.position.p_y - startDragY) * zoomP;
                        startDragX = event.position.p_x - (event.position.p_x - startDragX);
                        startDragY = event.position.p_y - (event.position.p_y - startDragY);
                        updateZoomAndPosition();
                        
                        break;
                    case "leave":
                        moving = null;
                        state = 50;
                        break;
                }
                break;

            case 55:  // moving piece
                if (!event) return;
                if (!moving){
                    state = 50;
                    return;
                }

                
                switch (event.event) {
                    case "move":
                        const event2_x = event.position.x;
                        const event2_y = event.position.y;
                        moving.xMouse = event2_x;
                        moving.yMouse = event2_y;
                        let to_x = event2_x - moving.xMouseInit + moving.ppXInit;
                        let to_y = event2_y - moving.yMouseInit + moving.ppYInit;


                        
                        moving.pp.moveTo(to_x, to_y);
                        moving.pp.moveAwayFromBorder();
                        moving.pp.hasMovedEver = true;
                        if (window.gameplayStarted && !window.play_solo) {
                            // console.log("move piece", moving.pp.pieces[0].index, moving.pp);                 
                            if(window.rotations == 0){
                                change_savedata_datastorage(moving.pp.pieces[0].index, [to_x / puzzle.contWidth, to_y / puzzle.contHeight], false);
                            }else{
                                change_savedata_datastorage(moving.pp.pieces[0].index, [to_x / puzzle.contWidth, to_y / puzzle.contHeight, moving.pp.rot], false);
                            }    
                        }

                        break;
                    case "leave":
                        // check if moved polypiece is close to a matching other polypiece
                        // check repeatedly since polypieces moved by merging may come close to other polypieces

                        for (let k = puzzle.polyPieces.length - 1; k >= 0; --k) {
                            // console.log(k)
                            let pp = puzzle.polyPieces[k];
                            if (pp == moving.pp || pp.pieces[0].index < 0 || moving.pp.pieces[0].index < 0) continue; // don't match with myself
                            if (moving.pp.ifNear(pp)) { // a match !
                                // compare polypieces sizes to move smallest one
                                console.log("found something!")
                                if (pp.pieces.length > moving.pp.pieces.length || (pp.pieces.length == moving.pp.pieces.length && pp.pieces[0].index > moving.pp.pieces[0].index)) {
                                    pp.merge(moving.pp);
                                    moving.pp = pp; // memorize piece to follow
                                } else {
                                    moving.pp.merge(pp);
                                }
                                console.log("done merging")
                            }
                        } // for k

                        if (window.gameplayStarted && !window.play_solo) {
                            
                            if(window.rotations == 0){
                                change_savedata_datastorage(moving.pp.pieces[0].index, [moving.pp.x / puzzle.contWidth, moving.pp.y / puzzle.contHeight], true);
                            }else{
                                change_savedata_datastorage(moving.pp.pieces[0].index, [moving.pp.x / puzzle.contWidth, moving.pp.y / puzzle.contHeight, moving.pp.rot], true);
                            }    
                            
                            const currentPieceIndex = moving.pp.pieces[0].index;
                            window.ignore_bounce_pieces.push(currentPieceIndex);
                            setTimeout(() => {
                                const index = window.ignore_bounce_pieces.indexOf(currentPieceIndex);
                                if (index !== -1) {
                                    window.ignore_bounce_pieces.splice(index, 1);
                                }
                            }, 1000);
                        }

                        

                        moving = null;

                        // not at its right place
                        puzzle.evaluateZIndex();
                        state = 50;
                        
                        return;
                } // switch (event.event)

                break;

            case 8888:
                return;


            case 9999: break;
            default:
                let st = state;
                state = 9999;  // to display message beyond only once
                throw ("oops, unknown state " + st);
        } // switch(state)
    } // animate
} // scope for animate
//-----------------------------------------------------------------------------

/* analyze menu */
let menu = (function () {
    let menu = { items: [] };
    document.querySelectorAll("#menu li").forEach(menuEl => {
    let kItem = menu.items.length;
    let item = { element: menuEl, kItem: kItem };
    menu.items[kItem] = item;

    });

    menu.open = function () {
    if(!gameStarted){
        document.getElementById("m1").style.display = "block"
        document.getElementById("m2").style.display = "block"
        document.getElementById("m3").style.display = "block"
        document.getElementById("m4").style.display = "block"
        document.getElementById("m5").style.display = "block"
        document.getElementById("m10b").style.display = "block"
        document.getElementById("o1a").style.display = "block";
        document.getElementById("o1b").style.display = "block";
    }
    document.getElementById("m6").style.display = "block"
    document.getElementById("m11").style.display = "inline-block"
    document.getElementById("m11a").style.display = "inline-block"
    if(gameStarted){
        document.getElementById("m9a").style.display = "block"
        document.getElementById("m9").style.display = "block"
        document.getElementById("m10").style.display = "block"

        console.log(window.show_clue)
        if(window.show_clue){
            document.getElementById("m13").style.display = "inline-block"
            document.getElementById("m13b").style.display = "inline-block"
            document.getElementById("m13c").style.display = "inline-block"
        }
    }
    menu.opened = true;
    }
    menu.close = function () {
    menu.items.forEach((item, k) => {
        if (k > 0) item.element.style.display = "none"; // never hide element 0
    });
    menu.opened = false;
    }
    document.getElementById("m0").addEventListener("click", () => {
        if (!window.play_solo && !window.is_connected) return;
        if (menu.opened) menu.close(); else menu.open()
    });
    return menu;
})();

document.getElementById("m1").addEventListener("click", loadInitialFile);
document.getElementById("m2").addEventListener("click", loadFile);
document.getElementById("m3").addEventListener("click", () => { });
document.getElementById("m4").addEventListener("click", () => events.push({ event: "nbpieces", nbpieces: 81 }));

document.getElementById("m5").addEventListener("click", () => {
    window.open('credits.html', '_blank');
});

document.getElementById("m13").addEventListener("click", () => {  
    askForHint(false);
});
let hint_color = "red";
document.getElementById("m13b").addEventListener("click", () => {  
    if(hint_color == "red"){
        hint_color = "green";
        document.getElementById("m13b").style.backgroundColor = "#00ff00";
    }else if(hint_color == "green"){
        hint_color = "blue";
        document.getElementById("m13b").style.backgroundColor = "#0000ff";
    }else{
        hint_color = "red";
        document.getElementById("m13b").style.backgroundColor = "#ff0000";
    }
});
document.getElementById("m13c").addEventListener("click", () => {  
    removeAllHints();
});


document.getElementById("m10b").addEventListener("click", () => {   
    const forPuzzleElement = document.getElementById("forPuzzle");     
    const red = document.getElementById("bgcolorR").value;
    const green = document.getElementById("bgcolorG").value;
    const blue = document.getElementById("bgcolorB").value;
    const newColor = `#${red}${green}${blue}`;
    forPuzzleElement.style.backgroundColor = newColor;
    localStorage.setItem("backgroundColor", newColor);

    // const jsonList = [{ type: "text", text: "Example text with new background" }];
    // window.jsonListener("", jsonList);
});

// Set the initial background color from localStorage if available
window.addEventListener("load", () => {
    let color = localStorage.getItem("backgroundColor");
    if (color === null) {
        color = "#DD9";
    }
    
    document.getElementById("forPuzzle").style.backgroundColor = color;
    document.getElementById("bgcolorR").value = color.slice(1, 2);
    document.getElementById("bgcolorG").value = color.slice(2, 3);
    document.getElementById("bgcolorB").value = color.slice(3, 4);
});


menu.open();

let resizeTimeout = null
window.addEventListener("resize", event => {
    if (resizeTimeout) {
        clearTimeout(resizeTimeout);
    }
    resizeTimeout = setTimeout(() => {
        events.push({ event: "resize" });
        resizeTimeout = null;
    }, 300);
});

const forPuzzle = document.getElementById('forPuzzle');
window.additional_zoom = 1;

function updateZoomAndPosition() {
    const puzzle = document.getElementById('forPuzzle');

    // Extract scale and translate values using regex
    const scaleFactor = 1 / parseFloat(getComputedStyle(document.documentElement).getPropertyValue('--scale-factor'));
    
    // Build the new transform string
    const newTransform = `
        translate(calc(-50% * (1 - ${scaleFactor})), -50%)
        scale(${scaleFactor})

        translate(${zoomX*100}%, ${zoomY*100}%)
        scale(${zoomP})
    `;

    // Apply the new transform
    puzzle.style.transform = newTransform;
    window.additional_zoom = zoomP;
}

let startDragX = 0;
let startDragY = 0;
let zoomX = 0;
let zoomY = 0;
let zoomP = 1;
forPuzzle.addEventListener('wheel', (event) => {
    if(moving){
        rotateCurrentPiece(event.deltaY < 0);
    }else{
        if(!allow_zoom){
            return;
        }
        event.preventDefault();
        if (event.deltaY < 0) {
            if(zoomP == 1){
                const co = puzzle.relativeMouseCoordinates(event);
                zoomX = -co.p_x + 1/2;
                zoomY = -co.p_y + 1/2;
                zoomP = 2;
            }else{
                const co = puzzle.relativeMouseCoordinates(event);
                zoomX = 2 * (-co.p_x + 1/2);
                zoomY = 2 * (-co.p_y + 1/2);
                zoomP = 3;
            }
        } else {
            zoomX = 0;
            zoomY = 0;
            zoomP = 1;
        }
        updateZoomAndPosition();
    }

});

let lastTap = 0;
forPuzzle.addEventListener('touchend', (event) => {
    if (event.touches.length != 0) return;
    const currentTime = new Date().getTime();
    const tapLength = currentTime - lastTap;
    if (tapLength < 300 && tapLength > 0) {
        event.preventDefault();
        if(!allow_zoom){
            return;
        }
        const co = puzzle.relativeMouseCoordinates(event.changedTouches[0]);
        if (window.additional_zoom === 1) {
            zoomX = -co.p_x + 1/2;
            zoomY = -co.p_y + 1/2;
            zoomP = 2;
        } else if(window.additional_zoom === 2) {
            zoomX = 2 * (-co.p_x + 1/2);
            zoomY = 2 * (-co.p_y + 1/2);
            zoomP = 3;
        } else{
            zoomX = 0;
            zoomY = 0;
            zoomP = 1;
        }
        updateZoomAndPosition();
    }
    lastTap = currentTime;
});








puzzle = new Puzzle({ container: "forPuzzle" });

requestAnimationFrame(animate);

// ap stuff:

var apnx;
var apny;
function set_puzzle_dim(x, y){
    apnx = x;
    apny = y;
    document.getElementById("m9a").innerText = "Merges: " + numberOfMerges + "/" + (apnx * apny - 1);
}
window.set_puzzle_dim = set_puzzle_dim


function findPolyPieceUsingPuzzlePiece(index, needsToBeFirst = false){
    for (let i = 0; i < puzzle.polyPieces.length; i++) {
        if(needsToBeFirst){
            if(puzzle.polyPieces[i].pieces[0].index == index){
                return puzzle.polyPieces[i];
            }
        }else{
            if (puzzle.polyPieces[i].pieces.some(piece => piece.index === index)) {
                return puzzle.polyPieces[i];
            }
        }
    }
    return null;
}

var puzzle_ini = false;
var unlocked_pieces = [];

function unlockPiece(index) {
    unlocked_pieces.push(index);

    if(process_pending_actions){
        let pp = findPolyPieceUsingPuzzlePiece(index);
        if(!pp){
            console.log("PolyPiece not found for index", index);
            return;
        }
        pp.moveTo(
            ((index+10)*43.2345) % (0.05 * puzzle.contWidth) - puzzle.scalex * 0.5,
            ((index+10)*73.6132) % (0.05 * puzzle.contHeight) - puzzle.scaley * 0.5
        );
        if (window.rotations > 0) {
            let num_rots = Math.round(360 / window.rotations);
            let random_rotation = 0;
            if (window.rotations == 180){
                random_rotation = Math.floor(2 * Math.floor(((index+10) * 2345.1234) % 2));
            }else{
                random_rotation = Math.floor(((index+10) * 2345.1234) % num_rots);
            }
            pp.rotateTo(random_rotation);
        }
        pp.unlocked = true;
    }else if (accept_pending_actions){
        console.log("Adding to pending actions", index)
        pending_actions.push([`x_x_x_${index}`, "unlock", "x"]);
    }
}

var unlocked_fake_pieces = [];
function unlockFakePiece() {
    if(unlocked_fake_pieces.length >= window.fake_pieces_mimic.length){
        console.log("No more fake pieces to unlock!");
        return;
    }
    let index = - unlocked_fake_pieces.length - 1;
    unlocked_fake_pieces.push(index);
    console.log("unlock fake piece", index)
    
    if(process_pending_actions){
        let pp = findPolyPieceUsingPuzzlePiece(index);
        console.log(pp)
        pp.moveTo(
            ((index+10)*429.2345) % (0.05 * puzzle.contWidth) - puzzle.scalex * 0.5,
            ((index+10)*723.6132) % (0.05 * puzzle.contHeight) - puzzle.scaley * 0.5
        );
        if (window.rotations > 0) {
            let num_rots = Math.round(360 / window.rotations);
            let random_rotation = 0;
            if (window.rotations == 180){
                random_rotation = Math.floor(2 * Math.floor(((index+10) * 2345.1234) % 2));
            }else{
                random_rotation = Math.floor(((index+10) * 2345.1234) % num_rots);
                pp.rotateTo(random_rotation);
            }
        }
        pp.unlocked = true;
    }else if (accept_pending_actions){
        console.log("Adding to pending actions", index)
        pending_actions.push([`x_x_x_${index}`, "unlock", "x"]);
        console.log(pending_actions)
    }
    console.log(puzzle.polyPieces)
}

function doSwapTrap(){
    let pps = getRandomPiece(2, 10);
    if(pps.length < 2) return;
    let pp1 = pps[0];
    let pp2 = pps[1];
    let x1 = pp1.x;
    let y1 = pp1.y;
    let x2 = pp2.x;
    let y2 = pp2.y;
    pp1.moveTo(x2, y2);
    pp2.moveTo(x1, y1);
    pp1.moveAwayFromBorder();
    pp2.moveAwayFromBorder();
    if(window.rotations == 0){
        change_savedata_datastorage(pp1.pieces[0].index, [pp1.x / puzzle.contWidth, pp1.y / puzzle.contHeight], true);
        change_savedata_datastorage(pp2.pieces[0].index, [pp2.x / puzzle.contWidth, pp2.y / puzzle.contHeight], true);
    }else{
        change_savedata_datastorage(pp1.pieces[0].index, [pp1.x / puzzle.contWidth, pp1.y / puzzle.contHeight, pp1.rot], true);
        change_savedata_datastorage(pp2.pieces[0].index, [pp2.x / puzzle.contWidth, pp2.y / puzzle.contHeight, pp2.rot], true);
    }   
}
function doRotateTrap(){
    let pps = getRandomPiece(1, 10);
    if(pps.length < 1) return;
    let pp = pps[0];
    if(window.rotations > 0){
        if(window.rotations == 180){
            pp.rotate(false, 2);
        }else{
            let num_rots = Math.round(360 / window.rotations);
            pp.rotate(false, Math.round(Math.random() * (num_rots)));
        }
        pp.moveAwayFromBorder();
        change_savedata_datastorage(pp.pieces[0].index, [pp.x / puzzle.contWidth, pp.y / puzzle.contHeight, pp.rot], true);
    }
}

function getRandomPiece(numberOfPieces, maxcluster) {

    // Get all PolyPieces that have only one piece (i.e., not merged)
    if(!puzzle || !puzzle.polyPieces) return [];
    const singlePieces = puzzle.polyPieces.filter(pp => pp.pieces.length <= maxcluster);
    const singleUnlockedPieces = singlePieces.filter(pp => pp.unlocked);
    // Shuffle the array
    const shuffled = singleUnlockedPieces.sort(() => Math.random() - 0.5);
    // Return up to numberOfPieces PolyPieces
    return shuffled.slice(0, numberOfPieces);
}

function updateMergesLabels(){
    try {
        document.getElementById("m9").innerText = "Merges in logic: " + (window.possible_merges[unlocked_pieces.length] !== undefined ? window.possible_merges[unlocked_pieces.length] : "?");
    } catch (e) {
        document.getElementById("m9").innerText = "Merges in logic: ?";
    }
    try {
        document.getElementById("m10").innerText = "Merges possible: " + (window.actual_possible_merges[unlocked_pieces.length] !== undefined ? window.actual_possible_merges[unlocked_pieces.length] : "?");
    } catch (e) {
        document.getElementById("m10").innerText = "Merges possible: ?";
    }
}

window.unlockPiece = unlockPiece;
window.unlockFakePiece = unlockFakePiece;
window.updateMergesLabels = updateMergesLabels;
window.doSwapTrap = doSwapTrap;
window.doRotateTrap = doRotateTrap;

var mergedKeys = [];

function newMerge(key, playSound = true){
    if (mergedKeys.includes(key)) return;
    mergedKeys.push(key);
    
    let newRecord = false;
    
    numberOfMerges += 1;
    
    if(numberOfMerges > numberOfMergesAtStart){
        window.sendCheck(numberOfMerges);
        // console.log("Send check for", numberOfMerges)
        if(numberOfMerges == apnx * apny - 1){
            window.sendGoal();
        }
        newRecord = true;
    }
        
    if(newRecord){
        change_savedata_datastorage("M", numberOfMerges, true);
    }
    document.getElementById("m9a").innerText = "Merges: " + numberOfMerges + "/" + (apnx * apny - 1);
    if(playSound){
        window.playNewMergeSound();
    }
}

var numberOfMerges = 0;
var numberOfMergesAtStart = 0;


function setImagePath(l){
    imagePath = l;
    document.getElementById("previm").src = imagePath;
    puzzle.srcImage.src = imagePath;
    console.log("SET!");
    loadImageFunction();
}

window.setImagePath = setImagePath;

function move_piece_bounced(data){ // pp_index, x, y, (r)
    do_action(`x_x_x_${data[0]}`, data[1], window.zero_list, true);
}

window.move_piece_bounced = move_piece_bounced;

async function change_savedata_datastorage(key, value, final) {
    // console.log("change_savedata_datastorage", key, value, final);
    
    if(window.play_solo) return;

    const key_name = `JIG_PROG_${window.slot}_${key}`;

    if (key == "M" || key == "O") {
        const client = window.getAPClient();
        client.storage.prepare(key_name, 0).replace(value).commit();
        return;
    }
    
    if(final){ //make sure you only replace it to lower values.
        const client = window.getAPClient();
        let currentValue = 0;
        currentValue = await client.storage.fetch([key_name], true);
        currentValue = currentValue[key_name];
        console.log("currentValue", currentValue, key_name)
        if (currentValue === null) {
            client.storage.prepare(key_name, window.zero_list).replace(value).commit();
        } else if (Array.isArray(currentValue) && Array.isArray(value)) {
            // Only replace if both are lists
            client.storage.prepare(key_name, window.zero_list).replace(value).commit();
        } else if (typeof currentValue === "number" && typeof value === "number") {
            // Replace only if value < currentValue
            client.storage.prepare(key_name, 999999).replace(Math.min(currentValue, value)).commit();
        } else if (!Array.isArray(value)) {
            // If X is not a list, replace the current value
            client.storage.prepare(key_name, window.zero_list).replace(value).commit();
        }
    }else{
        const client = window.getAPClient();
        if (!window.bounceTimeout) {
            // console.log("sending bounce", [key, value[0], value[1]])
            client.bounce({"slots": [window.slot]}, [key, value]);
            window.bounceTimeout = setTimeout(() => {
                window.bounceTimeout = null;
            }, 1000);
        }
    }
}

let pending_actions = []
function do_action(key, value, oldValue, bounce){
    // console.log("got response", key, value, oldValue, bounce);
    if(accept_pending_actions){
        if(!bounce){
            pending_actions.push([key, value, oldValue]);
            console.log("Add pending action", key, value, pending_actions)
        }
    } else if(process_pending_actions) {
        let pp_index = parseInt(key.split("_")[3]);
        let moving_that_piece = moving && moving.pp && moving.pp.pieces && moving.pp.pieces[0].index == pp_index;

        const pp = findPolyPieceUsingPuzzlePiece(pp_index, true);
        if(!pp){
            console.log("Ignore action not found", pp, pp_index)
            return;
        }
        if (Array.isArray(value) || value == "unlock") {
            if(moving_that_piece){
                return;
            }
            let [x,y,r] = [0,0,0];
            if(value == "unlock"){
                let num_rots = Math.round(360 / window.rotations);
                if (window.rotations == 0) num_rots = 1;
                let random_rotation = 0;
                if (window.rotations == 180){
                    random_rotation = Math.floor(2 * Math.floor((index * 2345.1234) % 2));
                }else{
                    random_rotation = Math.floor((index * 2345.1234) % num_rots);
                }
                [x,y,r] = 
                    [
                        ((pp_index+10)*43.2345) % 0.05,
                        ((pp_index+10)*73.6132) % 0.05,
                        random_rotation
                    ];
            }else{
                if (value.length == 3) {
                    [x, y, r] = value;
                } else if (value.length == 2) {
                    [x, y] = value;
                    r = 0;
                }
            }
            if (pp) {
                if(!bounce || (bounce && !window.ignore_bounce_pieces.includes(pp_index))){
                    // console.log("moving because of action", key, value, bounce);
                    pp.moveTo(x * puzzle.contWidth, y * puzzle.contHeight);
                    pp.rotateTo(r);
                    pp.hasMovedEver = true;
                }
            }
        } else { // value is an int
            value = parseInt(value);
            if (typeof oldValue === "number") return; //already merged!

            if(moving_that_piece || (moving && moving.pp && moving.pp.pieces && moving.pp.pieces[0].index == value)){
                moving = null; // let go of piece if someone else merges it...
            }
            const pp2 = findPolyPieceUsingPuzzlePiece(value);
            if(pp != pp2){
                console.log("merging because of action", key, value, bounce)
                if (pp.pieces.length > pp2.pieces.length  || (pp.pieces.length == pp2.pieces.length && pp.pieces[0].index > pp2.pieces[0].index)) {
                    pp.merge(pp2);
                } else {
                    pp2.merge(pp);
                }
            }
        }
    }
}

function removeAllHints(){
    puzzle.polyPieces.forEach(pp => {
        if(pp.hinted){
            pp.hinted = false;
            pp.polypiece_drawImage(false);
            // pp.polypiece_canvas.classList.remove('hinted')
        }
    });
}

function askForHint(alsoConnect = false){
    if(!window.play_solo && !window.is_connected) return;
    const shuffledIndices = [...Array(puzzle.polyPieces.length).keys()].sort(() => Math.random() - 0.5);
    for (let i = 0; i < shuffledIndices.length; i++) {
        for (let j = i + 1; j < shuffledIndices.length; j++) {
            let k = shuffledIndices[i];
            let l = shuffledIndices[j];

            let pp1 = puzzle.polyPieces[k];
            let pp2 = puzzle.polyPieces[l];
            if (pp1 == pp2) continue; // don't match with myself
            if (!pp1.unlocked) continue;
            if (!pp2.unlocked) continue;
            if (pp1.pieces[0].index < 0) continue;
            if (pp2.pieces[0].index < 0) continue;
            
            if (pp1.ifNear(pp2, true, true)) { // a match !
                console.log("MATCH FOUND!", pp1, pp2);
                if(!alsoConnect){
                    if(!pp1.hinted){
                        pp1.hinted = true;
                        pp1.polypiece_drawImage(false);
                        // pp1.polypiece_canvas.classList.add('hinted')
                        return;
                    }
                    if(!pp2.hinted){
                        pp2.hinted = true;
                        pp2.polypiece_drawImage(false);
                        // pp2.polypiece_canvas.classList.add('hinted')
                        return;
                    }
                }else{
                    // compare polypieces sizes to move smallest one
                    if (pp1.pieces.length > pp2.pieces.length  || (pp1.pieces.length == pp2.pieces.length && pp1.pieces[0].index > pp2.pieces[0].index)) {
                        pp1.merge(pp2);
                        console.log(pp1)
                    } else {
                        pp2.merge(pp1);
                        console.log(pp2)
                    }
                    console.log('merged')
                    return;
                }
            }
        }
    } // for k
    document.getElementById("m13").textContent = "That's it💡";
    setTimeout(() => {
        document.getElementById("m13").textContent = "Clue 💡✏️";
    }, 2000);
}


function rotateCurrentPiece(counter = false){
    if(!moving || typeof moving === 'undefined'){
        return;
    }
    if(!moving.pp){
        console.log("SOMETHING WEIRD HAPPENS?", moving)
        return;
    }

    // console.log(moving, counter)
    if(window.rotations > 0){
        if(window.rotations == 180){
            moving.pp.rotate(moving, 2);
        }else{
            if(counter){
                moving.pp.rotate(moving, -1);
            }else{
                moving.pp.rotate(moving);
            }
        }
        change_savedata_datastorage(moving.pp.pieces[0].index, [moving.pp.x / puzzle.contWidth, moving.pp.y / puzzle.contHeight, moving.pp.rot], false);
    }
    
}

document.addEventListener('keydown', function(event) {
    if(event.key === 'R' || event.key === 'r' || event.key === ' '){
        rotateCurrentPiece();
    }
});


// debug :)
document.addEventListener('keydown', function(event) {
    return;
    if(!window.debug || !puzzle || !puzzle.polyPieces) return;
    if (event.key === 'S' || event.key === 's' || event.key === 'H' || event.key === 'h') {
        const hint = event.key === 'H' || event.key === 'h';
        askForHint(!hint);
    }
    if(event.key === 'Q' || event.key === 'q'){
        window.goTo8888State = true;
    }
    if (event.key === 'D' || event.key === 'd') {
        doRotateTrap();
    }
    if (event.key === 'A' || event.key === 'a') {
        const interval = () => {
            setTimeout(() => {
            askForHint(true);
            interval();
            }, 100);
        };
        interval();
    }
});

// drawer

function withdraw(numToWithdraw){
    if (puzzle && puzzle.polyPieces) {
        // Get the number of pieces to withdraw from the select dropdown
        let piecesToWithdraw = puzzle.polyPieces.filter(pp => !pp.hasMovedEver && pp.unlocked && !pp.withdrawn);

        if (numToWithdraw !== "all") {
            numToWithdraw = parseInt(numToWithdraw, 10);
            // Shuffle and take only the requested number
            piecesToWithdraw = piecesToWithdraw.sort(() => Math.random() - 0.5).slice(0, numToWithdraw);
        }

        piecesToWithdraw.forEach(pp => {
            pp.moveTo(-10 * puzzle.contWidth, -10 * puzzle.contHeight);
            pp.withdrawn = true;
        });
        // Update the value of the span with id "pcsStored" to count
        const pcsStoredSpan = document.getElementById('pcsStored');
        if (pcsStoredSpan) {
            const am = puzzle.polyPieces.filter(pp => !pp.hasMovedEver && pp.unlocked && pp.withdrawn).length
            pcsStoredSpan.textContent = am;
            if (am > 0) {
                // Hide the control button with id "control-btn3a"
                const btn = document.getElementById('control-btn3a');
                if (btn) {
                    btn.style.display = "none";
                }
                pcsStoredSpan.style.color = "red";
                pcsStoredSpan.style.fontWeight = "bold";
            }
        }
        
    }
}

document.addEventListener('DOMContentLoaded', function() {
    const btnWithdraw = document.getElementById('btnWithdraw');
    const btnWithdrawAll = document.getElementById('btnWithdrawAll');
    const btnDeposit = document.getElementById('btnDeposit');
    btnWithdraw.addEventListener('click', function() {
        let numToWithdraw = document.getElementById('numPieces').value;
        withdraw(numToWithdraw);
    });
    btnWithdrawAll.addEventListener('click', function() {
        withdraw("all");
    });
    btnDeposit.addEventListener('click', function() {
        const select = document.getElementById('depositPosition');
        const value = select.value;

        if (puzzle && puzzle.polyPieces) {
            let x = 0, y = 0;
            switch (value) {
                case "1": // Top-left corner
                    x = 0.1;
                    y = 0.1;
                    break;
                case "2": // Top-left area
                    x = 0.3;
                    y = 0.3;
                    break;
                case "3": // Top edge
                    x = 0.7;
                    y = 0.1;
                    break;
                case "4": // Top area
                    x = 0.7;
                    y = 0.3;
                    break;
                case "5": // Left edge
                    x = 0.1;
                    y = 0.7;
                    break;
                case "6": // Left area
                    x = 0.3;
                    y = 0.7;
                    break;
                case "7": // Anywhere
                default:
                    x = 0.7;
                    y = 0.7;
                    break;
            }
            // Get the number of pieces to deposit from the select dropdown
            let numToDeposit = document.getElementById('numPieces').value;
            let piecesToDeposit = puzzle.polyPieces.filter(pp => !pp.hasMovedEver && pp.unlocked && pp.withdrawn);

            if (numToDeposit !== "all") {
                numToDeposit = parseInt(numToDeposit, 10);
                // Shuffle and take only the requested number
                piecesToDeposit = piecesToDeposit.sort(() => Math.random() - 0.5).slice(0, numToDeposit);
            }

            piecesToDeposit.forEach(pp => {
                pp.moveTo(Math.random() * x * puzzle.contWidth, Math.random() * y * puzzle.contHeight);
                pp.withdrawn = false;
            });

            // Update the value of the span with id "pcsStored" to count
            const pcsStoredSpan = document.getElementById('pcsStored');
            if (pcsStoredSpan) {
                let am = puzzle.polyPieces.filter(pp => !pp.hasMovedEver && pp.unlocked && pp.withdrawn).length
                pcsStoredSpan.textContent = am;
                
                if (am == 0) {
                    // Hide the control button with id "control-btn3a"
                    const btn = document.getElementById('control-btn3a');
                    if (btn) {
                        btn.style.display = "block";
                    }
                    pcsStoredSpan.style.color = "black"
                    pcsStoredSpan.style.fontWeight = "normal";
                }
            }
        }
    });
    
});