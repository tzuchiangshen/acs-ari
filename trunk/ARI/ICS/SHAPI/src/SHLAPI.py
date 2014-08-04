# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.4
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.



from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_SHLAPI', [dirname(__file__)])
        except ImportError:
            import _SHLAPI
            return _SHLAPI
        if fp is not None:
            try:
                _mod = imp.load_module('_SHLAPI', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _SHLAPI = swig_import_helper()
    del swig_import_helper
else:
    import _SHLAPI
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0



def SHAPI_Close(*args):
  return _SHLAPI.SHAPI_Close(*args)
SHAPI_Close = _SHLAPI.SHAPI_Close

def SHAPI_CheckFirmware(*args):
  return _SHLAPI.SHAPI_CheckFirmware(*args)
SHAPI_CheckFirmware = _SHLAPI.SHAPI_CheckFirmware

def SHAPI_GetTemperature(*args):
  return _SHLAPI.SHAPI_GetTemperature(*args)
SHAPI_GetTemperature = _SHLAPI.SHAPI_GetTemperature

def SHAPI_GetStructSize():
  return _SHLAPI.SHAPI_GetStructSize()
SHAPI_GetStructSize = _SHLAPI.SHAPI_GetStructSize

def SHAPI_SetPreamp(*args):
  return _SHLAPI.SHAPI_SetPreamp(*args)
SHAPI_SetPreamp = _SHLAPI.SHAPI_SetPreamp

def SHAPI_IsPreampAvailable(*args):
  return _SHLAPI.SHAPI_IsPreampAvailable(*args)
SHAPI_IsPreampAvailable = _SHLAPI.SHAPI_IsPreampAvailable

def SHAPI_GetFMFFTPK(*args):
  return _SHLAPI.SHAPI_GetFMFFTPK(*args)
SHAPI_GetFMFFTPK = _SHLAPI.SHAPI_GetFMFFTPK

def SHAPI_GetAudioFFTSample(*args):
  return _SHLAPI.SHAPI_GetAudioFFTSample(*args)
SHAPI_GetAudioFFTSample = _SHLAPI.SHAPI_GetAudioFFTSample

def SHAPI_GetSerNum(*args):
  return _SHLAPI.SHAPI_GetSerNum(*args)
SHAPI_GetSerNum = _SHLAPI.SHAPI_GetSerNum

def SHAPI_SyncTriggerMode(*args):
  return _SHLAPI.SHAPI_SyncTriggerMode(*args)
SHAPI_SyncTriggerMode = _SHLAPI.SHAPI_SyncTriggerMode

def SHAPI_CyclePowerOnExit(*args):
  return _SHLAPI.SHAPI_CyclePowerOnExit(*args)
SHAPI_CyclePowerOnExit = _SHLAPI.SHAPI_CyclePowerOnExit

def SHAPI_GetAMFFTPK(*args):
  return _SHLAPI.SHAPI_GetAMFFTPK(*args)
SHAPI_GetAMFFTPK = _SHLAPI.SHAPI_GetAMFFTPK

def SHAPI_ActivateAudioFFT(*args):
  return _SHLAPI.SHAPI_ActivateAudioFFT(*args)
SHAPI_ActivateAudioFFT = _SHLAPI.SHAPI_ActivateAudioFFT

def SHAPI_DeactivateAudioFFT(*args):
  return _SHLAPI.SHAPI_DeactivateAudioFFT(*args)
SHAPI_DeactivateAudioFFT = _SHLAPI.SHAPI_DeactivateAudioFFT

def SHAPI_GetRBW(*args):
  return _SHLAPI.SHAPI_GetRBW(*args)
SHAPI_GetRBW = _SHLAPI.SHAPI_GetRBW

def SHAPI_GetLastChannelPower(*args):
  return _SHLAPI.SHAPI_GetLastChannelPower(*args)
SHAPI_GetLastChannelPower = _SHLAPI.SHAPI_GetLastChannelPower

def SHAPI_GetLastChannelFreq(*args):
  return _SHLAPI.SHAPI_GetLastChannelFreq(*args)
SHAPI_GetLastChannelFreq = _SHLAPI.SHAPI_GetLastChannelFreq

def SHAPI_SetOscRatio(*args):
  return _SHLAPI.SHAPI_SetOscRatio(*args)
SHAPI_SetOscRatio = _SHLAPI.SHAPI_SetOscRatio

def SHAPI_Initialize(*args):
  return _SHLAPI.SHAPI_Initialize(*args)
SHAPI_Initialize = _SHLAPI.SHAPI_Initialize

def SHAPI_WriteCalTable(*args):
  return _SHLAPI.SHAPI_WriteCalTable(*args)
SHAPI_WriteCalTable = _SHLAPI.SHAPI_WriteCalTable

def SHAPI_CopyCalTable(*args):
  return _SHLAPI.SHAPI_CopyCalTable(*args)
SHAPI_CopyCalTable = _SHLAPI.SHAPI_CopyCalTable

def SHAPI_InitializeEx(*args):
  return _SHLAPI.SHAPI_InitializeEx(*args)
SHAPI_InitializeEx = _SHLAPI.SHAPI_InitializeEx

def SHAPI_SetAttenuator(*args):
  return _SHLAPI.SHAPI_SetAttenuator(*args)
SHAPI_SetAttenuator = _SHLAPI.SHAPI_SetAttenuator

def SHAPI_SelectExt10MHz(*args):
  return _SHLAPI.SHAPI_SelectExt10MHz(*args)
SHAPI_SelectExt10MHz = _SHLAPI.SHAPI_SelectExt10MHz

def SHAPI_Configure(*args):
  return _SHLAPI.SHAPI_Configure(*args)
SHAPI_Configure = _SHLAPI.SHAPI_Configure

def SHAPI_ConfigureFast(*args):
  return _SHLAPI.SHAPI_ConfigureFast(*args)
SHAPI_ConfigureFast = _SHLAPI.SHAPI_ConfigureFast

def SHAPI_GetSlowSweepCount(*args):
  return _SHLAPI.SHAPI_GetSlowSweepCount(*args)
SHAPI_GetSlowSweepCount = _SHLAPI.SHAPI_GetSlowSweepCount

def SHAPI_GetSlowSweep(*args):
  return _SHLAPI.SHAPI_GetSlowSweep(*args)
SHAPI_GetSlowSweep = _SHLAPI.SHAPI_GetSlowSweep

def SHAPI_GetFastSweepCount(*args):
  return _SHLAPI.SHAPI_GetFastSweepCount(*args)
SHAPI_GetFastSweepCount = _SHLAPI.SHAPI_GetFastSweepCount

def SHAPI_CyclePort(*args):
  return _SHLAPI.SHAPI_CyclePort(*args)
SHAPI_CyclePort = _SHLAPI.SHAPI_CyclePort

def SHAPI_GetFastSweep(*args):
  return _SHLAPI.SHAPI_GetFastSweep(*args)
SHAPI_GetFastSweep = _SHLAPI.SHAPI_GetFastSweep

def SHAPI_GetIQDataPacket(*args):
  return _SHLAPI.SHAPI_GetIQDataPacket(*args)
SHAPI_GetIQDataPacket = _SHLAPI.SHAPI_GetIQDataPacket

def SHAPI_Authenticate(*args):
  return _SHLAPI.SHAPI_Authenticate(*args)
SHAPI_Authenticate = _SHLAPI.SHAPI_Authenticate

def SHAPI_SetupLO(*args):
  return _SHLAPI.SHAPI_SetupLO(*args)
SHAPI_SetupLO = _SHLAPI.SHAPI_SetupLO

def SHAPI_StartStreamingData(*args):
  return _SHLAPI.SHAPI_StartStreamingData(*args)
SHAPI_StartStreamingData = _SHLAPI.SHAPI_StartStreamingData

def SHAPI_StopStreamingData(*args):
  return _SHLAPI.SHAPI_StopStreamingData(*args)
SHAPI_StopStreamingData = _SHLAPI.SHAPI_StopStreamingData

def SHAPI_GetStreamingPacket(*args):
  return _SHLAPI.SHAPI_GetStreamingPacket(*args)
SHAPI_GetStreamingPacket = _SHLAPI.SHAPI_GetStreamingPacket

def SHAPI_GetPhaseStep(*args):
  return _SHLAPI.SHAPI_GetPhaseStep(*args)
SHAPI_GetPhaseStep = _SHLAPI.SHAPI_GetPhaseStep

def SHAPI_GetIntFFT(*args):
  return _SHLAPI.SHAPI_GetIntFFT(*args)
SHAPI_GetIntFFT = _SHLAPI.SHAPI_GetIntFFT

def SHAPI_SetupFastSweepLoop(*args):
  return _SHLAPI.SHAPI_SetupFastSweepLoop(*args)
SHAPI_SetupFastSweepLoop = _SHLAPI.SHAPI_SetupFastSweepLoop

def SHAPI_GetFSLoopIQSize(*args):
  return _SHLAPI.SHAPI_GetFSLoopIQSize(*args)
SHAPI_GetFSLoopIQSize = _SHLAPI.SHAPI_GetFSLoopIQSize

def SHAPI_GetFSLoopIQ(*args):
  return _SHLAPI.SHAPI_GetFSLoopIQ(*args)
SHAPI_GetFSLoopIQ = _SHLAPI.SHAPI_GetFSLoopIQ

def SHAPI_ProcessFSLoopData(*args):
  return _SHLAPI.SHAPI_ProcessFSLoopData(*args)
SHAPI_ProcessFSLoopData = _SHLAPI.SHAPI_ProcessFSLoopData

def SHAPI_GetChannelPower(*args):
  return _SHLAPI.SHAPI_GetChannelPower(*args)
SHAPI_GetChannelPower = _SHLAPI.SHAPI_GetChannelPower

def SHAPI_RunMeasurementReceiver(*args):
  return _SHLAPI.SHAPI_RunMeasurementReceiver(*args)
SHAPI_RunMeasurementReceiver = _SHLAPI.SHAPI_RunMeasurementReceiver
# This file is compatible with both classic and new-style classes.

