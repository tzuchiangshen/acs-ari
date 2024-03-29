# **********************************************************************
#
# Copyright (c) 2003-2011 ZeroC, Inc. All rights reserved.
#
# This copy of Ice is licensed to you under the terms described in the
# ICE_LICENSE file included in this distribution.
#
# **********************************************************************
#
# Ice version 3.4.2
#
# <auto-generated>
#
# Generated from file `SRTcontrol.ice'
#
# Warning: do not edit this file.
#
# </auto-generated>
#

import Ice, IcePy, __builtin__

# Start of module SRTControl
_M_SRTControl = Ice.openModule('SRTControl')
__name__ = 'SRTControl'

if not _M_SRTControl.__dict__.has_key('telescope'):
    _M_SRTControl.telescope = Ice.createTempClass()
    class telescope(Ice.Object):
        def __init__(self):
            if __builtin__.type(self) == _M_SRTControl.telescope:
                raise RuntimeError('SRTControl.telescope is an abstract class')

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::SRTControl::telescope')

        def ice_id(self, current=None):
            return '::SRTControl::telescope'

        def ice_staticId():
            return '::SRTControl::telescope'
        ice_staticId = staticmethod(ice_staticId)

        def SRTinit(self, s, current=None):
            pass

        def __str__(self):
            return IcePy.stringify(self, _M_SRTControl._t_telescope)

        __repr__ = __str__

    _M_SRTControl.telescopePrx = Ice.createTempClass()
    class telescopePrx(Ice.ObjectPrx):

        def SRTinit(self, s, _ctx=None):
            return _M_SRTControl.telescope._op_SRTinit.invoke(self, ((s, ), _ctx))

        def begin_SRTinit(self, s, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_SRTControl.telescope._op_SRTinit.begin(self, ((s, ), _response, _ex, _sent, _ctx))

        def end_SRTinit(self, _r):
            return _M_SRTControl.telescope._op_SRTinit.end(self, _r)

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_SRTControl.telescopePrx.ice_checkedCast(proxy, '::SRTControl::telescope', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_SRTControl.telescopePrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

    _M_SRTControl._t_telescopePrx = IcePy.defineProxy('::SRTControl::telescope', telescopePrx)

    _M_SRTControl._t_telescope = IcePy.defineClass('::SRTControl::telescope', telescope, (), True, None, (), ())
    telescope._ice_type = _M_SRTControl._t_telescope

    telescope._op_SRTinit = IcePy.Operation('SRTinit', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), IcePy._t_string),), (), None, ())

    _M_SRTControl.telescope = telescope
    del telescope

    _M_SRTControl.telescopePrx = telescopePrx
    del telescopePrx

# End of module SRTControl
