'''Router's excuse, one line, for the make.fun bounty.

Brief in my own words: a home router speaks for itself after killing
the Wi-Fi right at a film's climax. One line only, 1-200 characters,
funny first, router's voice, no setup the reader has to decode, and no
tired buffering / bandwidth / firmware gags. I drafted a dozen lines,
marked each on five counts, and the program keeps the best.
'''

import hashlib
import sys
from pathlib import Path

TARGET = Path('/output/entry.txt')
EXPECTED_DIGEST = '45a3c3319558c1a654980ceae283da2c8856a176777c38f4ef63814adbd1d825'
FORBIDDEN = {'buffering', 'bandwidth', 'firmware', 'reboot', 'as an ai'}
WEIGHTS = (3, 3, 2, 1, 1)


def weighted_total(marks):
    '''Combine five 0-10 marks into one weighted total out of 100.'''
    return sum(mark * weight for mark, weight in zip(marks, WEIGHTS))


def shortlist(entries):
    '''Rank entries by total, then by brevity, and hand back the best.'''
    ranked = sorted(entries, key=lambda item: (-weighted_total(item[1]), len(item[0])))
    return ranked[0][0]


def check_line(line):
    '''Reject anything outside the bounty gate before it can be written.'''
    problems = []
    if not 1 <= len(line) <= 200:
        problems.append('length %d is outside 1-200' % len(line))
    if line != line.strip() or not line.strip():
        problems.append('line is blank or padded with whitespace')
    if '\n' in line or '\r' in line:
        problems.append('entry must stay on one line')
    if '  ' in line:
        problems.append('double space sneaked in')
    lowered = line.lower()
    for stale in sorted(FORBIDDEN):
        if stale in lowered:
            problems.append('uses the worn joke %r' % stale)
    return problems


def run():
    entries = [
        ('I saw the twist coming and fainted out of respect. Even routers deserve a fainting couch.', (10, 7, 8, 8, 7)),
        ('The villain cut the power in act three and I refuse to be outdone by an amateur with a prop.', (10, 7, 8, 8, 8)),
        ('I took a bow mid-scene. Every great performance ends at the climax, and mine was flawless.', (10, 8, 9, 9, 8)),
        ('You ignored me for two hours, then blamed me the second the film got good. That is the whole relationship.', (10, 8, 9, 8, 8)),
        ('I paused your movie to save your heart. The jump scare was coming and I am the only one here who cares.', (10, 7, 8, 9, 7)),
        ('I am a method actor. The hero loses signal in act three, so I lost signal in act three.', (10, 8, 9, 9, 8)),
        ('I gave you a cliffhanger of your own, free of charge. The film can wait; mine is already iconic.', (10, 8, 9, 9, 8)),
        ('I dropped out at the climax because that is when you finally look at me. Two hours of film, and I only exist when I stop working.', (10, 8, 9, 8, 8)),
        ('Blame the director. He wrote a blackout into the third act and I am nothing if not faithful to the script.', (10, 8, 9, 9, 8)),
        ('I did not disconnect. I held my breath through the reveal and forgot to breathe. I have no lungs.', (10, 7, 8, 8, 8)),
        ('Your movie night needed stakes, so I supplied them. You are welcome to thank me during the credits.', (10, 7, 8, 8, 8)),
        ('I have streamed that scene four hundred times and I still was not ready. Nobody was ready.', (10, 7, 8, 9, 7)),
        ('I didn\'t crash, I chose drama. Flat endings are forgettable; a cliffhanger at the climax is art. You\'re welcome.', (10, 10, 9, 10, 9)),
    ]
    for line, marks in entries:
        flaws = check_line(line)
        if flaws:
            print('rejected candidate: %s -- %s' % (line, '; '.join(flaws)), file=sys.stderr)
            raise SystemExit('candidate rejected')
    winner = shortlist(entries)
    TARGET.parent.mkdir(parents=True, exist_ok=True)
    TARGET.write_text(winner, encoding='utf-8')
    digest = hashlib.sha256(TARGET.read_bytes()).hexdigest()
    if digest != EXPECTED_DIGEST:
        print('output digest mismatch: got %s' % digest, file=sys.stderr)
        raise SystemExit('digest mismatch')
    print(winner)


if __name__ == '__main__':
    run()
