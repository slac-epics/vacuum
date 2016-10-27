TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE
#=============================

#=============================

#PROD_IOC = vacuum 

# vacuum.dbd will be created and installed
DBD += vacuum.dbd

# vacuum.dbd will be made up from these files:
vacuum_DBD += base.dbd
vacuum_DBD += iocAdmin.dbd
vacuum_DBD += autosaveSupport.dbd
vacuum_DBD += asyn.dbd
vacuum_DBD += stream.dbd
vacuum_DBD += modbus.dbd
vacuum_DBD += modbusSupport.dbd
vacuum_DBD += ether_ip.dbd
vacuum_DBD += caPutLog.dbd

LIBRARY_IOC = vacuum

# <name>_registerRecordDeviceDriver.cpp will be created from <name>.dbd
LIB_SRCS += vacuum_registerRecordDeviceDriver.cpp
LIB_SRCS_DEFAULT += vacuumMain.cpp

# Add locally compiled object code
#vacuum_SRCS += dbSubExample.c

LIB_LIBS += devIocStats
LIB_LIBS += autosave
LIB_LIBS += ModBusTCPClnt
LIB_LIBS += modbus
LIB_LIBS += asyn
LIB_LIBS += stream
LIB_LIBS += ether_ip
LIB_LIBS += caPutLog
LIB_LIBS += $(EPICS_BASE_IOC_LIBS)

PROD_SYS_LIBS_DEFAULT += pcre

#===========================

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE

