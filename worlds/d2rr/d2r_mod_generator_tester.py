from .d2r_mod_generator import D2RModGenerator


def test():
    d2rmg = D2RModGenerator()

    d2rmg.generate_mod(
        mod_name="ap_dev",
        character_name="APDEV",
        character_class="test_class"
    )