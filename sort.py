def sort(width: float, height: float, length: float, mass: float) -> str:
    """
    Sort packages into the correct stack based on volume and mass.
    
    Args:
        width: package width in cm
        height: package height in cm
        length: package length in cm
        mass: package mass in kg
    
    Returns:
        "STANDARD", "SPECIAL", or "REJECTED"
    """
    volume = width * height * length
    
    bulky = volume >= 1_000_000 or width >= 150 or height >= 150 or length >= 150
    heavy = mass >= 20
    
    if bulky and heavy:
        return "REJECTED"
    elif bulky or heavy:
        return "SPECIAL"
    else:
        return "STANDARD"


# ---- Tests ----
if __name__ == "__main__":
    # Standard: not bulky, not heavy
    assert sort(50, 50, 50, 10) == "STANDARD"        # volume=125,000, mass=10
    assert sort(1, 1, 1, 0.1) == "STANDARD"           # tiny package
    
    # Special: bulky only (volume >= 1,000,000)
    assert sort(100, 100, 100, 10) == "SPECIAL"        # volume=1,000,000, not heavy
    assert sort(200, 50, 50, 5) == "SPECIAL"           # volume=500,000 but dimension >= 150
    
    # Special: heavy only
    assert sort(50, 50, 50, 20) == "SPECIAL"           # not bulky, mass=20
    assert sort(10, 10, 10, 25) == "SPECIAL"           # small but heavy
    
    # Rejected: both bulky and heavy
    assert sort(100, 100, 100, 20) == "REJECTED"       # volume=1,000,000 and mass=20
    assert sort(200, 200, 200, 50) == "REJECTED"       # very bulky and very heavy
    assert sort(150, 1, 1, 25) == "REJECTED"           # single dimension >= 150 and heavy
    
    # Edge cases
    assert sort(0, 0, 0, 0) == "STANDARD"              # zero dimensions
    assert sort(100, 100, 99.99, 19.99) == "STANDARD"  # just under both thresholds
    assert sort(100, 100, 100, 19.99) == "SPECIAL"     # exactly at volume threshold
    assert sort(99, 99, 99, 20) == "SPECIAL"            # exactly at mass threshold
    assert sort(150, 1, 1, 19) == "SPECIAL"             # exactly at dimension threshold
    
    print("All tests passed!")
