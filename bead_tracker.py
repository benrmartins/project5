import math
import stdio
import sys
from blob_finder import BlobFinder
from picture import Picture


# Entry point
def main():
    # Accept command-line arguments pixels (int), tau (float), and delta (float)
    pixels = int(sys.argv[1])
    tau = float(sys.argv[2])
    delta = float(sys.argv[3])
    frames = sys.argv[4:]

    # BlobFinder object and from it get a list of beads currBeads that have at least pixels
    blobFind = BlobFinder(Picture(frames[0]), tau)
    prevBeads = blobFind.getBeads(pixels)
    # For each bead currBead in currBeads, find a bead prevBead from prevBeads that is no further
    for i in range(1, len(frames)):
        blobFind = BlobFinder(Picture(frames[i]), tau)
        currBeads = blobFind.getBeads(pixels)
        for currBead in currBeads:
            close = math.inf
            # loop through all of the prevBead in prevBeads
            for prevBead in prevBeads:
                r = currBead.distanceTo(prevBead)
                # if such a bead is found, write its distance (string ’%.4f\n’) to currBead
                if r <= delta and r < close:
                    close = r
            # checks is closest to currBead
            if close != math.inf:
                stdio.writef('%.4f\n', close)
        stdio.writeln()
        # Sets previous beads to current beads.
        prevBeads = currBeads


if __name__ == '__main__':
    main()
