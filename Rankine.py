import numpy as np
from scipy.interpolate import griddata
from Steam import steam

class rankine():

    def __init__(self,p_low,p_high, t_high = None, name = 'Rankine Cycle'):
        self.p_low = p_low
        self.p_high = p_high
        self.t_high = t_high
        self.name = name
        self.efficiency = None
        self.turbine_work = 0
        self.pump_work = 0
        self.heat_added = 0
        self.state1 = None
        self.state2 = None
        self.state3 = None
        self.state4 = None

    def calc_efficiency(self):
        if self.t_high == None:
            self.state1 = steam(self.p_high, x = 1, name = 'Turbine Inlet')
        else:
            self.state1 = steam(self.p_high, T=self.t_high, name='Turbine Inlet')
        s2 = self.state1.s
        self.state2 = steam(self.p_low, s=s2, name='Turbine Exit')
        self.state3 = steam(self.p_low, x=0, name='Pump Inlet')
        self.state4 = steam(self.p_high, name='Pump Exit')
        h4 = self.state3.h + self.state3.v * (self.p_high - self.p_low)
        self.state4.h = h4
        self.turbine_work = self.state1.h - self.state2.h
        self.pump_work = self.state4.h - self.state3.h
        self.heat_added = self.state1.h - self.state4.h
        self.efficiency = (self.turbine_work - self.pump_work) / self.heat_added * 100
        return self.efficiency

    def print_summary (self):
        if self.efficiency == None:
            self.calc_efficiency()
        print('\n Cycle Summary for: ', self.name)
        print('\n Efficiency: {:.3f} %'.format(self.efficiency))
        print(' Turbine Work: {:.1f} kJ/kg'.format(self.turbine_work))
        print(' Pump Work: {:.2f} kJ/kg'.format(self.pump_work))
        print(' Heat Added: {:.1f} kJ/kg \n'.format(self.heat_added))
        self.state1.print()
        self.state2.print()
        self.state3.print()
        self.state4.print()


def main():
    rankine1 = rankine(8, 8000, t_high=500, name='Rankine Cycle - Superheated at turbine inlet')
    eff = rankine1.calc_efficiency()
    print(eff)
    rankine1.state3.print()

    rankine1.print_summary()

if __name__ == "__main__":
    main()