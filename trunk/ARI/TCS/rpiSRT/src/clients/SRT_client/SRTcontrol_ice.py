# **********************************************************************
#
# Copyright (c) 2003-2013 ZeroC, Inc. All rights reserved.
#
# This copy of Ice is licensed to you under the terms described in the
# ICE_LICENSE file included in this distribution.
#
# **********************************************************************
#
# Ice version 3.5.1
#
# <auto-generated>
#
# Generated from file `SRTcontrol.ice'
#
# Warning: do not edit this file.
#
# </auto-generated>
#

import Ice, IcePy

# Start of module SRTControl
_M_SRTControl = Ice.openModule('SRTControl')
__name__ = 'SRTControl'

if '_t_ports' not in _M_SRTControl.__dict__:
    _M_SRTControl._t_ports = IcePy.defineSequence('::SRTControl::ports', (), IcePy._t_string)

if '_t_spectrum' not in _M_SRTControl.__dict__:
    _M_SRTControl._t_spectrum = IcePy.defineSequence('::SRTControl::spectrum', (), IcePy._t_float)

if 'AntennaStatus' not in _M_SRTControl.__dict__:
    _M_SRTControl.AntennaStatus = Ice.createTempClass()
    class AntennaStatus(object):
        def __init__(self, az=0.0, el=0.0, aznow=0.0, elnow=0.0, axis=0, tostow=0, elatstow=0, azatstow=0, slew=0, serialport='', lastSRTCom='', lastSerialMsg=''):
            self.az = az
            self.el = el
            self.aznow = aznow
            self.elnow = elnow
            self.axis = axis
            self.tostow = tostow
            self.elatstow = elatstow
            self.azatstow = azatstow
            self.slew = slew
            self.serialport = serialport
            self.lastSRTCom = lastSRTCom
            self.lastSerialMsg = lastSerialMsg

        def __eq__(self, other):
            if other is None:
                return False
            elif not isinstance(other, _M_SRTControl.AntennaStatus):
                return NotImplemented
            else:
                if self.az != other.az:
                    return False
                if self.el != other.el:
                    return False
                if self.aznow != other.aznow:
                    return False
                if self.elnow != other.elnow:
                    return False
                if self.axis != other.axis:
                    return False
                if self.tostow != other.tostow:
                    return False
                if self.elatstow != other.elatstow:
                    return False
                if self.azatstow != other.azatstow:
                    return False
                if self.slew != other.slew:
                    return False
                if self.serialport != other.serialport:
                    return False
                if self.lastSRTCom != other.lastSRTCom:
                    return False
                if self.lastSerialMsg != other.lastSerialMsg:
                    return False
                return True

        def __ne__(self, other):
            return not self.__eq__(other)

        def __str__(self):
            return IcePy.stringify(self, _M_SRTControl._t_AntennaStatus)

        __repr__ = __str__

    _M_SRTControl._t_AntennaStatus = IcePy.defineStruct('::SRTControl::AntennaStatus', AntennaStatus, (), (
        ('az', (), IcePy._t_float),
        ('el', (), IcePy._t_float),
        ('aznow', (), IcePy._t_float),
        ('elnow', (), IcePy._t_float),
        ('axis', (), IcePy._t_int),
        ('tostow', (), IcePy._t_int),
        ('elatstow', (), IcePy._t_int),
        ('azatstow', (), IcePy._t_int),
        ('slew', (), IcePy._t_int),
        ('serialport', (), IcePy._t_string),
        ('lastSRTCom', (), IcePy._t_string),
        ('lastSerialMsg', (), IcePy._t_string)
    ))

    _M_SRTControl.AntennaStatus = AntennaStatus
    del AntennaStatus

if '_t_anst' not in _M_SRTControl.__dict__:
    _M_SRTControl._t_anst = IcePy.defineSequence('::SRTControl::anst', (), _M_SRTControl._t_AntennaStatus)

if 'specs' not in _M_SRTControl.__dict__:
    _M_SRTControl.specs = Ice.createTempClass()
    class specs(object):
        def __init__(self, spec=None, avspec=None, avspecc=None, specd=None):
            self.spec = spec
            self.avspec = avspec
            self.avspecc = avspecc
            self.specd = specd

        def __eq__(self, other):
            if other is None:
                return False
            elif not isinstance(other, _M_SRTControl.specs):
                return NotImplemented
            else:
                if self.spec != other.spec:
                    return False
                if self.avspec != other.avspec:
                    return False
                if self.avspecc != other.avspecc:
                    return False
                if self.specd != other.specd:
                    return False
                return True

        def __ne__(self, other):
            return not self.__eq__(other)

        def __str__(self):
            return IcePy.stringify(self, _M_SRTControl._t_specs)

        __repr__ = __str__

    _M_SRTControl._t_specs = IcePy.defineStruct('::SRTControl::specs', specs, (), (
        ('spec', (), _M_SRTControl._t_spectrum),
        ('avspec', (), _M_SRTControl._t_spectrum),
        ('avspecc', (), _M_SRTControl._t_spectrum),
        ('specd', (), _M_SRTControl._t_spectrum)
    ))

    _M_SRTControl.specs = specs
    del specs

if '_t_spectrums' not in _M_SRTControl.__dict__:
    _M_SRTControl._t_spectrums = IcePy.defineSequence('::SRTControl::spectrums', (), _M_SRTControl._t_specs)

if 'telescope' not in _M_SRTControl.__dict__:
    _M_SRTControl.telescope = Ice.createTempClass()
    class telescope(Ice.Object):
        def __init__(self):
            if Ice.getType(self) == _M_SRTControl.telescope:
                raise RuntimeError('SRTControl.telescope is an abstract class')

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::SRTControl::telescope')

        def ice_id(self, current=None):
            return '::SRTControl::telescope'

        def ice_staticId():
            return '::SRTControl::telescope'
        ice_staticId = staticmethod(ice_staticId)

        def message(self, s, current=None):
            pass

        def SRTGetSerialPorts(self, current=None):
            pass

        def SRTSetSerialPort(self, s, current=None):
            pass

        def SRTinit(self, s, current=None):
            pass

        def SRTStow(self, current=None):
            pass

        def SRTStatus(self, current=None):
            pass

        def SRTAzEl(self, az, el, current=None):
            pass

        def SRTThreads(self, current=None):
            pass

        def serverState(self, current=None):
            pass

        def SRTSetFreq(self, freq, receiver, current=None):
            pass

        def SRTGetSpectrum(self, current=None):
            pass

        def SRTDoCalibration(self, method, current=None):
            pass

        def __str__(self):
            return IcePy.stringify(self, _M_SRTControl._t_telescope)

        __repr__ = __str__

    _M_SRTControl.telescopePrx = Ice.createTempClass()
    class telescopePrx(Ice.ObjectPrx):

        def message(self, s, _ctx=None):
            return _M_SRTControl.telescope._op_message.invoke(self, ((s, ), _ctx))

        def begin_message(self, s, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_SRTControl.telescope._op_message.begin(self, ((s, ), _response, _ex, _sent, _ctx))

        def end_message(self, _r):
            return _M_SRTControl.telescope._op_message.end(self, _r)

        def SRTGetSerialPorts(self, _ctx=None):
            return _M_SRTControl.telescope._op_SRTGetSerialPorts.invoke(self, ((), _ctx))

        def begin_SRTGetSerialPorts(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_SRTControl.telescope._op_SRTGetSerialPorts.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_SRTGetSerialPorts(self, _r):
            return _M_SRTControl.telescope._op_SRTGetSerialPorts.end(self, _r)

        def SRTSetSerialPort(self, s, _ctx=None):
            return _M_SRTControl.telescope._op_SRTSetSerialPort.invoke(self, ((s, ), _ctx))

        def begin_SRTSetSerialPort(self, s, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_SRTControl.telescope._op_SRTSetSerialPort.begin(self, ((s, ), _response, _ex, _sent, _ctx))

        def end_SRTSetSerialPort(self, _r):
            return _M_SRTControl.telescope._op_SRTSetSerialPort.end(self, _r)

        def SRTinit(self, s, _ctx=None):
            return _M_SRTControl.telescope._op_SRTinit.invoke(self, ((s, ), _ctx))

        def begin_SRTinit(self, s, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_SRTControl.telescope._op_SRTinit.begin(self, ((s, ), _response, _ex, _sent, _ctx))

        def end_SRTinit(self, _r):
            return _M_SRTControl.telescope._op_SRTinit.end(self, _r)

        def SRTStow(self, _ctx=None):
            return _M_SRTControl.telescope._op_SRTStow.invoke(self, ((), _ctx))

        def begin_SRTStow(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_SRTControl.telescope._op_SRTStow.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_SRTStow(self, _r):
            return _M_SRTControl.telescope._op_SRTStow.end(self, _r)

        def SRTStatus(self, _ctx=None):
            return _M_SRTControl.telescope._op_SRTStatus.invoke(self, ((), _ctx))

        def begin_SRTStatus(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_SRTControl.telescope._op_SRTStatus.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_SRTStatus(self, _r):
            return _M_SRTControl.telescope._op_SRTStatus.end(self, _r)

        def SRTAzEl(self, az, el, _ctx=None):
            return _M_SRTControl.telescope._op_SRTAzEl.invoke(self, ((az, el), _ctx))

        def begin_SRTAzEl(self, az, el, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_SRTControl.telescope._op_SRTAzEl.begin(self, ((az, el), _response, _ex, _sent, _ctx))

        def end_SRTAzEl(self, _r):
            return _M_SRTControl.telescope._op_SRTAzEl.end(self, _r)

        def SRTThreads(self, _ctx=None):
            return _M_SRTControl.telescope._op_SRTThreads.invoke(self, ((), _ctx))

        def begin_SRTThreads(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_SRTControl.telescope._op_SRTThreads.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_SRTThreads(self, _r):
            return _M_SRTControl.telescope._op_SRTThreads.end(self, _r)

        def serverState(self, _ctx=None):
            return _M_SRTControl.telescope._op_serverState.invoke(self, ((), _ctx))

        def begin_serverState(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_SRTControl.telescope._op_serverState.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_serverState(self, _r):
            return _M_SRTControl.telescope._op_serverState.end(self, _r)

        def SRTSetFreq(self, freq, receiver, _ctx=None):
            return _M_SRTControl.telescope._op_SRTSetFreq.invoke(self, ((freq, receiver), _ctx))

        def begin_SRTSetFreq(self, freq, receiver, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_SRTControl.telescope._op_SRTSetFreq.begin(self, ((freq, receiver), _response, _ex, _sent, _ctx))

        def end_SRTSetFreq(self, _r):
            return _M_SRTControl.telescope._op_SRTSetFreq.end(self, _r)

        def SRTGetSpectrum(self, _ctx=None):
            return _M_SRTControl.telescope._op_SRTGetSpectrum.invoke(self, ((), _ctx))

        def begin_SRTGetSpectrum(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_SRTControl.telescope._op_SRTGetSpectrum.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_SRTGetSpectrum(self, _r):
            return _M_SRTControl.telescope._op_SRTGetSpectrum.end(self, _r)

        def SRTDoCalibration(self, method, _ctx=None):
            return _M_SRTControl.telescope._op_SRTDoCalibration.invoke(self, ((method, ), _ctx))

        def begin_SRTDoCalibration(self, method, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_SRTControl.telescope._op_SRTDoCalibration.begin(self, ((method, ), _response, _ex, _sent, _ctx))

        def end_SRTDoCalibration(self, _r):
            return _M_SRTControl.telescope._op_SRTDoCalibration.end(self, _r)

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_SRTControl.telescopePrx.ice_checkedCast(proxy, '::SRTControl::telescope', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_SRTControl.telescopePrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

    _M_SRTControl._t_telescopePrx = IcePy.defineProxy('::SRTControl::telescope', telescopePrx)

    _M_SRTControl._t_telescope = IcePy.defineClass('::SRTControl::telescope', telescope, -1, (), True, False, None, (), ())
    telescope._ice_type = _M_SRTControl._t_telescope

    telescope._op_message = IcePy.Operation('message', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), IcePy._t_string, False, 0),), (((), IcePy._t_string, False, 0),), None, ())
    telescope._op_SRTGetSerialPorts = IcePy.Operation('SRTGetSerialPorts', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (((), _M_SRTControl._t_ports, False, 0),), None, ())
    telescope._op_SRTSetSerialPort = IcePy.Operation('SRTSetSerialPort', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), IcePy._t_string, False, 0),), (((), IcePy._t_string, False, 0),), None, ())
    telescope._op_SRTinit = IcePy.Operation('SRTinit', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), IcePy._t_string, False, 0),), (((), IcePy._t_string, False, 0),), None, ())
    telescope._op_SRTStow = IcePy.Operation('SRTStow', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (((), IcePy._t_string, False, 0),), None, ())
    telescope._op_SRTStatus = IcePy.Operation('SRTStatus', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (((), _M_SRTControl._t_AntennaStatus, False, 0),), None, ())
    telescope._op_SRTAzEl = IcePy.Operation('SRTAzEl', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), IcePy._t_float, False, 0), ((), IcePy._t_float, False, 0)), (((), IcePy._t_string, False, 0),), None, ())
    telescope._op_SRTThreads = IcePy.Operation('SRTThreads', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (((), IcePy._t_string, False, 0),), None, ())
    telescope._op_serverState = IcePy.Operation('serverState', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (((), IcePy._t_string, False, 0),), None, ())
    telescope._op_SRTSetFreq = IcePy.Operation('SRTSetFreq', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), IcePy._t_float, False, 0), ((), IcePy._t_string, False, 0)), (((), IcePy._t_string, False, 0),), None, ())
    telescope._op_SRTGetSpectrum = IcePy.Operation('SRTGetSpectrum', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (((), _M_SRTControl._t_specs, False, 0),), None, ())
    telescope._op_SRTDoCalibration = IcePy.Operation('SRTDoCalibration', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), IcePy._t_string, False, 0),), (((), IcePy._t_float, False, 0),), None, ())

    _M_SRTControl.telescope = telescope
    del telescope

    _M_SRTControl.telescopePrx = telescopePrx
    del telescopePrx

# End of module SRTControl