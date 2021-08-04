from pylogix import PLC
with PLC() as comm:
    comm.IPAddress = '192.168.1.10'
    ret = comm.Read('VB.Position')
    comm.Write('VB.Velocity', 100)
    comm.Write('VB.Position', 2000)
    comm.Write('VB.Start',True)
    # comm.Write('VB.Stop',True)
    print(ret.TagName, ret.Value, ret.Status)