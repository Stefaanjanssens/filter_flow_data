import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel (r'C:\Users\s.janssens.CI\PycharmProjects\filter_flow_data\filtered_means combined.xlsx') #place "r" before the path string to address special character, such as '\'. Don't forget to put the file name at the end of the path + '.xlsx'
plt.figure(1)
#unique pressure setpoints
pressures=(df["Equilibar Read Pressure Setpoint"]).unique()

#plot sensirion flow in function of setpoint for 10slm flowcontroller and for the different set pressures
for p in pressures:
    df_p=df.loc[df["Equilibar Read Pressure Setpoint"]==p]
    plt.scatter(df_p['SFC5_10slm  Read Flow Setpoint'],df_p['SFC5_10slm  Read Flow'],label=f"p: {p}")
    plt.legend()

plt.xlim(0, 5.5)
plt.xlabel('flow setpoint (slm)')
plt.ylabel('flow SFC5_10slm (slm)')


#plot sensirion flow in function of setpoint for 0.5slm flowcontroller and for the different set pressures
plt.figure(2)
pressures=(df["Equilibar Read Pressure Setpoint"]).unique()
for p in pressures:
    df_p=df.loc[df["Equilibar Read Pressure Setpoint"]==p]
    plt.scatter(df_p['SFC5_0.5slm  Read Flow Setpoint'],df_p['SFC5_0.5slm  Read Flow'],label=f"p: {p}",alpha=0.25)
    plt.legend()

plt.xlim(-0.1, 0.6)
plt.xlabel('flow setpoint (slm)')
plt.ylabel('flow SFC5_0.5slm (slm)')

#plot Smart trak flow meter M1 flow in function of setpoint  and for the different set pressures
plt.figure(3)
pressures=(df["Equilibar Read Pressure Setpoint"]).unique()
for p in pressures:
    df_p=df.loc[df["Equilibar Read Pressure Setpoint"]==p]
    plt.scatter(df_p['setpoint'],df_p['filtered M1'],label=f"p: {p}",alpha=0.5)
    plt.legend()

plt.xlim(-0.1, 5.5)
plt.ylim(-0.1, 6)
plt.xlabel('flow setpoint (slm)')
plt.ylabel('flow Smart Trak M1 (slm)')

#plot Smart trak flow Controller C1 flow in function of setpoint and for the different set pressures
plt.figure(4)
pressures=(df["Equilibar Read Pressure Setpoint"]).unique()
for p in pressures:
    df_p=df.loc[df["Equilibar Read Pressure Setpoint"]==p]
    plt.scatter(df_p['setpoint'],df_p['filtered C1'],label=f"p: {p}",alpha=0.5)
    plt.legend()

plt.xlim(-0.1, 5.5)
plt.ylim(-0.1, 6)
plt.xlabel('flow setpoint (slm)')
plt.ylabel('flow Smart Trak C1 (slm)')

#plot Smart trak flow Controller C2 flow in function of setpoint and for the different set pressures
plt.figure(5)
pressures=(df["Equilibar Read Pressure Setpoint"]).unique()
for p in pressures:
    df_p=df.loc[df["Equilibar Read Pressure Setpoint"]==p]
    plt.scatter(df_p['setpoint'],df_p['filtered C2'],label=f"p: {p}",alpha=0.5)
    plt.legend()

plt.xlim(-0.1, 5.5)
plt.ylim(-0.1, 6)
plt.xlabel('flow setpoint (slm)')
plt.ylabel('flow Smart Trak C2 (slm)')


plt.show()


