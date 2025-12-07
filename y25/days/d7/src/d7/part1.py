from common import parse_file


def run():
    data = parse_file(7).splitlines()
    beams = {data.pop(0).index('S')}

    result = 0
    for row in data:
        splitters = [i for i, ch in enumerate(row) if ch == '^']
        new_beams = set()
        for beam in beams:
            if beam in splitters:
                new_beams |= {beam-1, beam+1}
                result += 1
            else:
                new_beams.add(beam)
        beams = new_beams

    return result
