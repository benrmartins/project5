import math
import stdio


# Entry point.
def main():
    # Initialize ETA, RHO, T, and R to appropriate values.
    ETA = 9.135e-4
    RHO = 5e-7
    T = 297.0
    R = 8.31457
    METERS_PER_PIXEL = 1.75e-7

    # Calculate var as the sum of the squares of the n displacements read from standard
    displacements = stdio.readAllFloats()
    var = sum(map(lambda r: (METERS_PER_PIXEL * r) ** 2, displacements)) / (2 * len(displacements))

    # Estimates Boltzmann’s constant as 6 * math.pi * var * ETA * RHO /
    BOLTZMANN = 6 * math.pi * var * ETA * RHO / T

    # Estimate Avogadro’s constant as R / k
    AVOGADRO = R / BOLTZMANN
    # output the two constants in scientific notation and separated by a space.
    stdio.writef('%e %e\n', BOLTZMANN, AVOGADRO)


if __name__ == '__main__':
    main()
