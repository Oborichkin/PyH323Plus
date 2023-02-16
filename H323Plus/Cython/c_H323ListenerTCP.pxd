include "ptlib.pxi"

from H323Plus.Cython.c_H323EndPoint cimport c_H323EndPoint
from PTLib.Cython.c_Address cimport c_Address

cdef extern from "transports.h":
    cdef cppclass c_H323ListenerTCP "H323ListenerTCP":
        c_H323ListenerTCP(c_H323EndPoint &endpoint, c_Address binding, WORD port, PBoolean exclusive)
