#from Steam import steam
from Rankine import rankine


def main():
    """
        A test program for rankine power cycles.
        R1 is a rankine cycle object that is instantiated for turbine inlet of saturated vapor.
        R2 is a rankine cycle object that is instantiated for turbine inlet of superheated vapor.
        :return: none
        """
    rankine1 = rankine(8, 8000, t_high=500, name='Rankine Cycle - Superheated at turbine inlet')
    # t_high is specified
    # if t_high were not specified, then x_high = 1 is assumed
    eff = rankine1.calc_efficiency()
    print(eff)
    rankine1.state3.print()
    rankine1.print_summary()
    # hf=rankine1.state1.hf
    # hg=rankine1.state1.hg
    rankine2 = rankine(8, 8000, name='Rankine Cycle - Saturated at turbine inlet')
    eff2 = rankine2.calc_efficiency()
    print(eff2)

    rankine2.print_summary()


if __name__ == "__main__":
    main()