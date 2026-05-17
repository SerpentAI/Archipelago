"use strict";

// var downsize_to_fit = localStorage.getItem("option_downsize");
// if (downsize_to_fit === null) downsize_to_fit = 0.85;
var downsize_to_fit = 0.85;
var accept_pending_actions = false;
var process_pending_actions = false;

var bevel_size = localStorage.getItem("option_bevel_2");
if (bevel_size === null) bevel_size = 0.1;

var shadow_size = localStorage.getItem("option_shadow_2");
if (shadow_size === null) shadow_size = 0;


window.save_loaded = false;
window.ignore_bounce_pieces = [];

var puzzle;

let seed = 1;

function random() {
    const x = Math.sin(seed++) * 10000;
    return x - Math.floor(x);
}

function setRandomSeed(newSeed) {
    seed = newSeed;
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

function twist0(side, ca, cb) {

    const seg0 = new Segment(side.points[0], side.points[1]);
    const dxh = seg0.dx();
    const dyh = seg0.dy();

    const seg1 = new Segment(ca, cb);
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

function twist1(side, ca, cb) {

    const seg0 = new Segment(side.points[0], side.points[1]);
    const dxh = seg0.dx();
    const dyh = seg0.dy();

    const seg1 = new Segment(ca, cb);
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

function twist2(side, ca, cb) {

    const seg0 = new Segment(side.points[0], side.points[1]);
    const dxh = seg0.dx();
    const dyh = seg0.dy();

    const seg1 = new Segment(ca, cb);
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

function twist3(side, ca, cb) {

    side.points = [side.points[0], side.points[1]];

} // twist3

function twist4(side, ca, cb) {
    side.points[0].x = Math.round(side.points[0].x)
    side.points[0].y = Math.round(side.points[0].y)
    side.points[1].x = Math.round(side.points[1].x)
    side.points[1].y = Math.round(side.points[1].y)
    side.points = [side.points[0], side.points[1]];

} // twist3


//-----------------------------------------------------------------------------
class Piece {
    constructor(kx, ky, index) { // object with 4 sides
        this.ts = new Side(); // top side
        this.rs = new Side(); // right side
        this.bs = new Side(); // bottom side
        this.ls = new Side(); // left side
        this.kx = kx;
        this.ky = ky;
        this.index = index;
        this.drawn = false;
    }

    //- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    piece_scale(puzzle) {
        this.ts.side_scale(puzzle);
        this.rs.side_scale(puzzle);
        this.bs.side_scale(puzzle);
        this.ls.side_scale(puzzle);
    } // Piece.scale
} // class Piece
//--------------------------------------------------------------
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
        // console.log("Call merge", this.pieces[0].index, otherPoly.pieces[0].index);
        if(this == otherPoly){
            return;
        }

        const orgpckxmin = this.pckxmin;
        const orgpckymin = this.pckymin;

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

        this.moveTo(this.x + this.puzzle.scalex * (this.pckxmin - orgpckxmin),
            this.y + this.puzzle.scaley * (this.pckymin - orgpckymin));

        // if(window.gameplayStarted){
        //     // console.log("move after merge")
        //     change_savedata_datastorage(this.pieces[0].index, [this.x / puzzle.contWidth, this.y / puzzle.contHeight], true);
        // }

        this.puzzle.evaluateZIndex();

        newMerge();


    } // merge

    // -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -   -
    ifNear(otherPoly, ignoreCloseness = false) {

        if(this.pieces.length > otherPoly.pieces.length){
            return otherPoly.ifNear(this, ignoreCloseness)
        }

        let puzzle = this.puzzle;

        // coordinates of origin of full picture for this PolyPieces
        let x = this.x - puzzle.scalex * this.pckxmin;
        let y = this.y - puzzle.scaley * this.pckymin;

        let ppx = otherPoly.x - puzzle.scalex * otherPoly.pckxmin;
        let ppy = otherPoly.y - puzzle.scaley * otherPoly.pckymin;

        if(!ignoreCloseness){
            if (mhypot(x - ppx, y - ppy) >= puzzle.dConnect) return false; // not close enough
        }

        // this and otherPoly are in good relative position, have they a common side ?
        let neighs = [];
        for (let k = this.pieces.length - 1; k >= 0; --k) {
            let p1 = this.pieces[k].index;
            if (p1 <= apnx * (apny - 1)) neighs.push(p1 + apnx)
            if (p1 > apnx) neighs.push(p1 - apnx)
            if (p1 % apnx != 1) neighs.push(p1 - 1)
            if (p1 % apnx != 0) neighs.push(p1 + 1)
        }
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
            let k;
            switch (edge) {
            case 0: ky--; break; // top edge
            case 1: kx++; break; // right edge
            case 2: ky++; break; // bottom edge
            case 3: kx--; break; // left edge
            } // switch
            for (k = 0; k < that.pieces.length; k++) {
            if (kx == that.pieces[k].kx && ky == that.pieces[k].ky) return true; // we found the neighbor
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
        let kEdge; // to count 4 edges
        let lp; // for loop during its creation
        let currEdge; // current edge
        let tries; // tries counter
        let edgeNumber; // number of edge found during research
        let potNext;

        // table of tries

        let tbTries = [
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
        ];

        // create list of not shared edges (=> belong to boundary)
        for (k = 0; k < this.pieces.length; k++) {
            for (kEdge = 0; kEdge < 4; kEdge++) {
            if (!edgeIsCommon(this.pieces[k].kx, this.pieces[k].ky, kEdge))
                tbEdges.push({ kx: this.pieces[k].kx, ky: this.pieces[k].ky, edge: kEdge, kp: k })
            } // for kEdge
        } // for k

        while (tbEdges.length > 0) {
            lp = []; // new loop
            currEdge = tbEdges[0];   // we begin with first available edge
            lp.push(currEdge);       // add it to loop
            tbEdges.splice(0, 1);    // remove from list of available sides
            do {
            for (tries = 0; tries < 3; tries++) {
                potNext = tbTries[currEdge.edge][tries];
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
            if (edge.edge == 0) return cell.ts;
            if (edge.edge == 1) return cell.rs;
            if (edge.edge == 2) return cell.bs;
            return cell.ls;
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


        // // make shadow
        // this.polypiece_ctx.fillStyle = 'none';
        // this.polypiece_ctx.shadowColor = 'rgba(0, 0, 0, 0.5)';
        // this.polypiece_ctx.shadowBlur = 32 * window.scaleFactor * window.additional_zoom * puzzle.scalex / 2700 * shadow_size * 2;
        // this.polypiece_ctx.shadowOffsetX = 32 * window.scaleFactor * window.additional_zoom * puzzle.scalex / 2700 * shadow_size * 2;
        // this.polypiece_ctx.shadowOffsetY = 32 * window.scaleFactor * window.additional_zoom * puzzle.scalex / 2700 * shadow_size * 2;
        
            
        // this.polypiece_ctx.fill(this.path);
        // this.polypiece_ctx.shadowColor = 'rgba(0, 0, 0, 0)'; // stop shadow effect


        this.pieces.forEach((pp, kk) => {

            if(!pp.drawn || !ignoreRedraw) {
                this.polypiece_ctx.save();

                const path = new Path2D();
                const shiftx = -this.offsx;
                const shifty = -this.offsy;
                pp.ts.drawPath(path, shiftx, shifty, false);
                pp.rs.drawPath(path, shiftx, shifty, true);
                pp.bs.drawPath(path, shiftx, shifty, true);
                pp.ls.drawPath(path, shiftx, shifty, true);
                path.closePath();
                

                this.polypiece_ctx.clip(path);
                // do not copy from negative coordinates, does not work for all browsers
                const srcx = pp.kx ? ((pp.kx - 0.5) * puzzle.scalex) : 0;
                const srcy = pp.ky ? ((pp.ky - 0.5) * puzzle.scaley) : 0;

                const destx = ( (pp.kx ? 0 : 1 / 2) + (pp.kx - this.pckxmin) ) * puzzle.scalex;
                const desty = ( (pp.ky ? 0 : 1 / 2) + (pp.ky - this.pckymin) ) * puzzle.scaley;

                let w = 2 * puzzle.scalex;
                let h = 2 * puzzle.scaley;
                // if (srcx + w > puzzle.gameCanvas.width) w = puzzle.gameCanvas.width - srcx;
                // if (srcy + h > puzzle.gameCanvas.height) h = puzzle.gameCanvas.height - srcy;

                let embth = puzzle.scalex * 0.01 * bevel_size * window.scaleFactor * window.additional_zoom;
                if(this.hinted){
                    embth = puzzle.scalex * 0.01 * window.scaleFactor * window.additional_zoom;
                }
                // console.log(embth)

                this.polypiece_ctx.drawImage(puzzle.gameCanvas, srcx, srcy, w, h, destx, desty, w, h);

                this.polypiece_ctx.translate(embth / 2, -embth / 2);
                this.polypiece_ctx.lineWidth = embth;
                this.polypiece_ctx.strokeStyle = "rgba(0, 0, 0, 0.35)";
                if(this.hinted){
                    this.polypiece_ctx.strokeStyle = "rgba(250, 0, 0, 1)";
                }
                this.polypiece_ctx.stroke(path);

                this.polypiece_ctx.translate(-embth, embth);
                this.polypiece_ctx.strokeStyle = "rgba(255, 255, 255, 0.35)";
                
                if(this.hinted){
                    this.polypiece_ctx.strokeStyle = "rgba(250, 0, 0, 1)";
                }
                this.polypiece_ctx.stroke(path);
                
                this.polypiece_ctx.restore();

                pp.drawn = true;
            }
        });


    } // PolyPiece.polypiece_drawImage


    moveTo(x, y) {
        // sets the left, top properties (relative to container) of this.canvas
        this.x = x;
        this.y = y;
        this.polypiece_canvas.style.left = (this.x) + 'px';
        this.polypiece_canvas.style.top = (this.y) + 'px';
    } //

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
            events.push({ event: 'touch', position: this.relativeMouseCoordinates(event) });
            // console.log(event);
        });
        this.container.addEventListener("touchstart", event => {
            event.preventDefault();
            if (event.touches.length != 1) return;
            let ev = event.touches[0];
            events.push({ event: 'touch', position: this.relativeMouseCoordinates(ev) });
        }, { passive: false });

        this.container.addEventListener("mouseup", event => {
            event.preventDefault();
            handleLeave();
        });
        this.container.addEventListener("touchend", handleLeave);
        this.container.addEventListener("touchleave", handleLeave);
        this.container.addEventListener("touchcancel", handleLeave);

        this.container.addEventListener("mousemove", event => {
            event.preventDefault();
            // do not accumulate move events in events queue - keep only current one
            if (events.length && events[events.length - 1].event == "move") events.pop();
            
            events.push({ event: 'move', position: this.relativeMouseCoordinates(event) })
        });
        this.container.addEventListener("touchmove", event => {
            event.preventDefault();
            if (event.touches.length != 1) return;
            let ev = event.touches[0];
            // do not accumulate move events in events queue - keep only current one
            if (events.length && events[events.length - 1].event == "move") events.pop();
            // console.log("touch", event.offsetX, event.offsetY, event)
            events.push({ event: 'move', position: this.relativeMouseCoordinates(ev) });
        }, { passive: false });

        /* create canvas to contain picture - will be styled later */
        this.gameCanvas = document.createElement('CANVAS');
        this.container.appendChild(this.gameCanvas)

        this.srcImage = new Image();
        this.imageLoaded = false;
        this.srcImage.addEventListener("load", () => imageLoaded(this));

        function handleLeave() {
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
    puzzle_create(coordinates, groups) {

        // Set the seed of Math.random to window.apseed
        if(window.apseed){
            setRandomSeed(window.apseed % 10000);
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

        this.defineShapes({ coeffDecentr: 0.12, twistf: [twist0, twist1, twist2, twist3, twist4][document.getElementById("shape").value - 1] });

        this.polyPieces = [];

        if(coordinates.length != groups.length){
            console.log("coordinates and groups do not have the same length?", coordinates, groups)
        }

        console.log("started making pieces")
        for (let key in coordinates) {
            let pieces_in_group = [];
            for (let ind of groups[key]) {
                let w = (ind-1) % window.apnx;
                let h = Math.floor((ind-1) / window.apnx);
                pieces_in_group.push(this.pieces[h][w]);
            }
            newMerge(pieces_in_group.length - 1);
            let ppp = new PolyPiece(pieces_in_group, this);
            ppp.moveTo(coordinates[key][0] * puzzle.contWidth, coordinates[key][1] * puzzle.contHeight)
            this.polyPieces.push(ppp);
        }
        console.log("done making pieces")

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

    let { coeffDecentr, twistf } = shapeDesc;

    const corners = [];
    const nx = this.nx, ny = this.ny;
    let np;

    for (let ky = -1; ky <= ny+1; ++ky) {
        corners[ky] = [];
        for (let kx = -1; kx <= nx+1; ++kx) {
        corners[ky][kx] = new Point(kx + alea(-coeffDecentr, coeffDecentr),
            ky + alea(-coeffDecentr, coeffDecentr));
        if (kx == 0) corners[ky][kx].x = 0;
        if (kx == nx) corners[ky][kx].x = nx;
        if (ky == 0) corners[ky][kx].y = 0;
        if (ky == ny) corners[ky][kx].y = ny;
        } // for kx
    } // for ky

    // Array of pieces
    this.pieces = [];
    for (let ky = 0; ky < ny; ++ky) {
        this.pieces[ky] = [];
        for (let kx = 0; kx < nx; ++kx) {
            this.pieces[ky][kx] = np = new Piece(kx, ky, ky * nx + kx + 1);
            // top side
            if (ky == 0) {
                np.ts.points = [corners[ky][kx], corners[ky][kx + 1]];
                np.ts.type = "d";
            } else {
                np.ts = this.pieces[ky - 1][kx].bs.reversed();
            }
            // right side
            np.rs.points = [corners[ky][kx + 1], corners[ky + 1][kx + 1]];
            np.rs.type = "d";
            if (kx < nx - 1) {
                if (intAlea(2)) // randomly twisted on one side of the side
                twistf(np.rs, corners[ky][kx], corners[ky + 1][kx]);
                else
                twistf(np.rs, corners[ky][kx + 2], corners[ky + 1][kx + 2]);
            }
            // left side
            if (kx == 0) {
                np.ls.points = [corners[ky + 1][kx], corners[ky][kx]];
                np.ls.type = "d";
            } else {
                np.ls = this.pieces[ky][kx - 1].rs.reversed()
            }
            // bottom side
            np.bs.points = [corners[ky + 1][kx + 1], corners[ky + 1][kx]];
            np.bs.type = "d";
            if (ky < ny - 1) {
                if (intAlea(2)) // randomly twisted on one side of the side
                twistf(np.bs, corners[ky][kx + 1], corners[ky][kx]);
                else
                twistf(np.bs, corners[ky + 2][kx + 1], corners[ky + 2][kx]);
            }
        } // for kx
    } // for ky

    } // Puzzle.defineShapes

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

        this.gameCtx.drawImage(
            this.srcImage, 
            0, 
            0, 
            this.gameWidth * downsize_to_fit, 
            this.gameHeight * downsize_to_fit
        ); //safe
        

        this.gameCanvas.classList.add("gameCanvas");
        this.gameCanvas.style.zIndex = 100000002;

        /* scale pieces */
        this.scalex = downsize_to_fit * this.gameWidth / this.nx;    // average width of pieces, add zoom here
        this.scaley = downsize_to_fit * this.gameHeight / this.ny;   // average height of pieces
        

        this.pieces.forEach(row => {
            row.forEach(piece => piece.piece_scale(this));
        }); // this.pieces.forEach, safe

        /* calculate offset for centering image in container */
        this.offsx = (this.contWidth - this.gameWidth) / 2;
        this.offsy = (this.contHeight - this.gameHeight) / 2;

        /* computes the distance below which two pieces connect
            depends on the actual size of pieces, with lower limit */
        this.dConnect = mmax(10, mmin(this.scalex, this.scaley) / 10) * window.scaleFactor * window.additional_zoom;



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
                fitImage(tmpImage, puzzle.contWidth * downsize_to_fit, puzzle.contHeight * downsize_to_fit);
            }
            else if (state >= 25) { // resize pieces
                
                const x_change = puzzle.contWidth / puzzle.prevWidth;
                const y_change = puzzle.contHeight / puzzle.prevHeight;

                puzzle.puzzle_scale();
                
                console.log("start scaling pieces")
                puzzle.polyPieces.forEach(pp => {                    
                    let nx = pp.x;
                    let ny = pp.y;

                    pp.moveTo(nx, ny);
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
                loadImageFunction();
                state = 15;
                return;


            /* wait for choice of number of pieces */
            case 15:
                if (event && event.event == "srcImageLoaded") {
                    // display centered initial image
                    loadImageFunction();
                    return;
                } 
                
                if ((event && event.event == "nbpieces") || (window.LoginStart && window.is_connected)) {
                    document.getElementById("m4").textContent = "Loading...";

                    state = 17;
                    if(window.is_connected){
                        imagePath = localStorage.setItem(`image_${window.apseed}_${window.slot}`, imagePath);
                    }
                }
                
                return;

            
            case 17: // load save!

                if(unlocked_pieces.length == 0){
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

                        let client = window.getAPClient();                  

                        await client.storage.notify(keys, (key, value, oldValue) => {
                            do_action(key, value, false);
                        });

                        keys.push(`JIG_PROG_${window.slot}_M`);
                        keys.push(`JIG_PROG_${window.slot}_O`);

                        let results = (await client.storage.fetch(keys, true))
                        console.log("results", results)
                        
                        for (let [key, value] of Object.entries(results)) {
                            let spl = key.split("_")[3];
                            if (spl === "O"){
                                if(value){
                                    if(Math.abs(parseFloat(value) - puzzle.srcImage.width / puzzle.srcImage.height) > 0.05){
                                        alert("Warning, you are not using the same aspect ratio as before. Pieces might not be in the correct relative position. You can refresh now to discard this login (if you do ignore this error next time).")
                                    }
                                }
                                change_savedata_datastorage("O", puzzle.srcImage.width / puzzle.srcImage.height, true);
                            }else{
                                if(value){
                                    if (spl === "M") {
                                        numberOfMergesAtStart = parseInt(value);
                                    }else {
                                        let pp_index = parseInt(spl);
                                        window.save_file[pp_index] = value;
                                    }
                                }
                            }
                            
                        }
                    }

                    unlocked_pieces.sort(() => Math.random() - 0.5).forEach(index => {
                        if (window.save_file[index] === undefined) {
                            window.save_file[index] = 
                            [
                                (index * 4321.1234) % 0.10, (index * 1234.4321) % 0.5
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

                let all_indices = []

                for (let key = 1; key <= window.apnx * window.apny; key++) {
                    all_indices.push(key);
                }

                for (let [key, value] of Object.entries(window.save_file)) {
                    all_indices = all_indices.filter(index => index !== parseInt(key));

                    if (Array.isArray(value)) {
                        coordinates[key] = value;
                        groups[key] = [parseInt(key)];
                    } else {
                        let refer_to = value;
                        let groupKey = Object.keys(groups).find(groupKey => groups[groupKey].includes(refer_to));
                        if (groupKey) {
                            groups[groupKey].push(parseInt(key));
                        } else {
                            console.log(refer_to, "not found")
                        }
                    }
                }

                for(let key of all_indices){
                    groups[key] = [key];
                    coordinates[key] = [3,3];
                }

                console.log("STARTING GAME")
                gameStarted = true;
                menu.open();

                document.getElementById("m1").style.display = "none";
                document.getElementById("m2").style.display = "none";
                document.getElementById("m3").style.display = "none";
                document.getElementById("m4").style.display = "none";
                document.getElementById("m5").style.display = "none";
                document.getElementById("m5a").style.display = "none";
                document.getElementById("m10b").style.display = "none";

                /* prepare puzzle */
                puzzle.puzzle_create(coordinates, groups); // create shape of pieces, independant of size



                puzzle_ini = true;

                console.log("done getting backlog of actions")
                
                puzzle.puzzle_scale();
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
                        do_action(data[0], data[1], false);
                    }
                } catch (error) {
                    console.error("Error processing pending actions:", error);
                    alert("Error while loading, please refresh the page (and I would appreciate a ping via discord with a screenshot of the debug panel (F12))")
                }


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
                
                if (event.event != "touch") return;

                const event_x = event.position.x;
                const event_y = event.position.y;
                // console.log(event_x, event_y)

                moving = {
                    xMouseInit: event_x,
                    yMouseInit: event_y
                }

                /* evaluates if contact inside a PolyPiece, by decreasing z-index */
                puzzle.polyPieces.sort((a, b) => a.polypiece_canvas.style.zIndex - b.polypiece_canvas.style.zIndex);
                for (let k = puzzle.polyPieces.length-1; k >= 0; k--) {
                    let pp = puzzle.polyPieces[k];
                    if (pp.polypiece_ctx.isPointInPath(pp.path, event_x - pp.x, event_y - pp.y)) {
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
                        // console.log(event2_x, event2_y)
                        let to_x = event2_x - moving.xMouseInit + moving.ppXInit;
                        let to_y = event2_y - moving.yMouseInit + moving.ppYInit;
                        to_x = mmin(
                            mmax(
                                to_x, 
                                - (moving.pp.nx-1) * puzzle.scalex
                            ),
                            puzzle.contWidth - puzzle.scalex
                        );
                        to_y = mmin(
                            mmax(
                                to_y, 
                                - (moving.pp.ny-1) * puzzle.scaley
                            ),
                            puzzle.contHeight - puzzle.scaley
                        );

                        
                        moving.pp.moveTo(to_x, to_y);
                        if (window.gameplayStarted && !window.play_solo) {
                            // console.log("move piece", moving.pp.pieces[0].index, moving.pp);                        
                            change_savedata_datastorage(moving.pp.pieces[0].index, [to_x / puzzle.contWidth, to_y / puzzle.contHeight], false);
                        }

                        break;
                    case "leave":
                        // check if moved polypiece is close to a matching other polypiece
                        // check repeatedly since polypieces moved by merging may come close to other polypieces

                        for (let k = puzzle.polyPieces.length - 1; k >= 0; --k) {
                            // console.log(k)
                            let pp = puzzle.polyPieces[k];
                            if (pp == moving.pp) continue; // don't match with myself
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
                            // console.log("move piece", moving.pp.pieces[0].index, moving.pp);                        
                            change_savedata_datastorage(moving.pp.pieces[0].index, [moving.pp.x / puzzle.contWidth, moving.pp.y / puzzle.contHeight], true);
                            
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
        document.getElementById("m5a").style.display = "block"
        
        document.getElementById("m10b").style.display = "block"
    }
    document.getElementById("m6").style.display = "block"
    if(gameStarted){
        document.getElementById("m9a").style.display = "block"
        document.getElementById("m9").style.display = "block"
        document.getElementById("m10").style.display = "block"
        document.getElementById("m13").style.display = "block"
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
document.getElementById("m5a").addEventListener("click", () => {
    window.open('options.html', '_blank');
});

document.getElementById("m13").addEventListener("click", () => {  
    askForHint(false);
});


document.getElementById("m10b").addEventListener("click", () => {   
    const forPuzzleElement = document.getElementById("forPuzzle");     
    const red = document.getElementById("bgcolorR").value;
    const green = document.getElementById("bgcolorG").value;
    const blue = document.getElementById("bgcolorB").value;
    const newColor = `#${red}${green}${blue}`;
    forPuzzleElement.style.backgroundColor = newColor;
    localStorage.setItem("backgroundColor", newColor);

    const jsonList = [{ type: "text", text: "Example text with new background" }];
    window.jsonListener("", jsonList);
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


function updatePreviewAndClient(){
    let element = document.getElementById("previm");
    element.style.width = widthsOfPreview[savedIndexPreview] + "vw";
    localStorage.setItem("widthOfPreviewIndex", savedIndexPreview);
    
    element = document.getElementById("log");
    element.style.width = Math.max(widthsOfClient[savedIndexClient], widthsOfPreview[savedIndexPreview]) + "vw";
    element.style.fontSize = textsizeOfClient[savedIndexClient] + "vw";
    localStorage.setItem("widthsOfClientIndex", savedIndexClient);

}


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
    event.preventDefault();
    if (event.deltaY < 0) {
        const co = puzzle.relativeMouseCoordinates(event);
        zoomX = -co.p_x + 1/2;
        zoomY = -co.p_y + 1/2;
        zoomP = 2;
        updateZoomAndPosition();
    } else {
        zoomX = 0;
        zoomY = 0;
        zoomP = 1;
        updateZoomAndPosition();
    }
});

let lastTap = 0;
forPuzzle.addEventListener('touchend', (event) => {
    console.log("HEYO")
    const currentTime = new Date().getTime();
    const tapLength = currentTime - lastTap;
    if (tapLength < 300 && tapLength > 0) {
        event.preventDefault();
        const co = puzzle.relativeMouseCoordinates(event.changedTouches[0]);
        if (window.additional_zoom === 1) {
            zoomX = -co.p_x + 1/2;
            zoomY = -co.p_y + 1/2;
            zoomP = 2;
            updateZoomAndPosition();
        } else {
            zoomX = 0;
            zoomY = 0;
            zoomP = 1;
            updateZoomAndPosition();
        }
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
        pp.moveTo(
            (index*43.2345) % (0.05 * puzzle.contWidth),
            (index*73.6132) % (0.05 * puzzle.contHeight)
        );
    }else if (accept_pending_actions){
        console.log("Adding to pending actions", index)
        pending_actions.push([`x_x_x_${index}`, "unlock"]);
    }
}

function updateMergesLabels(){
    document.getElementById("m9").innerText = "Merges in logic: " + window.possible_merges[unlocked_pieces.length];
    document.getElementById("m10").innerText = "Merges possible: " + window.actual_possible_merges[unlocked_pieces.length];
}

window.unlockPiece = unlockPiece;
window.updateMergesLabels = updateMergesLabels

function newMerge(add = 1){
    if(add < 1){
        return;
    }
    let newRecord = false;
    for(let i = 0; i < add; i++){
        numberOfMerges += 1;
        
        if(numberOfMerges > numberOfMergesAtStart){
            window.sendCheck(numberOfMerges);
            // console.log("Send check for", numberOfMerges)
            if(numberOfMerges == apnx * apny - 1){
                window.sendGoal();
            }
            newRecord = true;
        }
    }
    if(newRecord){
        change_savedata_datastorage("M", numberOfMerges, true);
    }
    document.getElementById("m9a").innerText = "Merges: " + numberOfMerges + "/" + (apnx * apny - 1);
    window.playNewMergeSound();
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

function move_piece_bounced(pp_index, x, y){
    do_action(`x_x_x_${pp_index}`, [x,y], true);
}

window.move_piece_bounced = move_piece_bounced;

function change_savedata_datastorage(key, value, final) {
    
    if(window.play_solo) return;
    // console.log(key, value, final)
    if(final){
        const client = window.getAPClient();
        // console.log("setting", `JIG_PROG_${window.slot}_${key}`, "to", value)
        client.storage.prepare(`JIG_PROG_${window.slot}_${key}`, 0).replace(value).commit();
    }else{
        const client = window.getAPClient();
        if (!window.bounceTimeout) {
            // console.log("sending bounce", [key, value[0], value[1]])
            client.bounce({"slots": [window.slot]}, [key, value[0], value[1]]);
            window.bounceTimeout = setTimeout(() => {
                window.bounceTimeout = null;
            }, 50);
        }
    }
}

let pending_actions = []
function do_action(key, value, bounce){
    console.log("got response", key, value, bounce);
    if(accept_pending_actions){
        if(!bounce){
            pending_actions.push([key, value]);
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
            let [x,y] = [0,0];
            if(value == "unlock"){
                [x,y] = 
                    [
                        (pp_index*43.2345) % 0.05,
                        (pp_index*73.6132) % 0.05
                    ];
            }else{
                [x, y] = value;
            }
            if (pp) {
                if(!bounce || (bounce && !window.ignore_bounce_pieces.includes(pp_index))){
                    console.log("moving because of action", key, value, bounce);
                    pp.moveTo(x * puzzle.contWidth, y * puzzle.contHeight);
                }
            }
        } else {
            value = parseInt(value);
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

function askForHint(alsoConnect = false){
    console.log("Let's go", alsoConnect)
    const shuffledIndices = [...Array(puzzle.polyPieces.length).keys()].sort(() => Math.random() - 0.5);
    for (let i = 0; i < shuffledIndices.length; i++) {
        for (let j = i + 1; j < shuffledIndices.length; j++) {
            let k = shuffledIndices[i];
            let l = shuffledIndices[j];

            let pp1 = puzzle.polyPieces[k];
            let pp2 = puzzle.polyPieces[l];
            if (pp1 == pp2) continue; // don't match with myself
            if (!unlocked_pieces.includes(pp1.pieces[0].index)) continue;
            if (!unlocked_pieces.includes(pp2.pieces[0].index)) continue;
            
            if (pp1.ifNear(pp2, true)) { // a match !
                if(!alsoConnect){
                    if(!pp1.hinted){
                        pp1.hinted = true;
                        pp1.polypiece_drawImage(false);
                        return;
                    }
                    if(!pp2.hinted){
                        pp2.hinted = true;
                        pp2.polypiece_drawImage(false);
                        return;
                    }
                }else{
                    // compare polypieces sizes to move smallest one
                    if (pp1.pieces.length > pp2.pieces.length  || (pp1.pieces.length == pp2.pieces.length && pp1.pieces[0].index > pp2.pieces[0].index)) {
                        pp1.merge(pp2);
                    } else {
                        pp2.merge(pp1);
                    }
                    console.log('merged')
                    return;
                }
            }
        }
    } // for k
    document.getElementById("m13").textContent = "That's it...";
    setTimeout(() => {
        document.getElementById("m13").textContent = "Hint";
    }, 2000);
}

window.debug = localStorage.getItem("debug") == "yes";

document.addEventListener('keydown', function(event) {
    if(!window.debug) return;
    if (event.key === 'S' || event.key === 's' || event.key === 'H' || event.key === 'h') {
        const hint = event.key === 'H' || event.key === 'h';
        askForHint(!hint);
    }
    if(event.key === 'Q' || event.key === 'q'){
        window.goTo8888State = true;
    }
});