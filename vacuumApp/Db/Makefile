TOP=../..
include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE

#----------------------------------------------------
#  Optimization of db files using dbst (DEFAULT: NO)
#DB_OPT = YES

#----------------------------------------------------
# Create and install (or just install)
# databases, templates, substitutions like this
DB_INSTALLS += $(IOCADMIN)/db/iocAdmin.db

DB += sync_master.db
DB += sync_mks937a_serial.template
DB += sync_mks937a_serial_cc.template
DB += sync_mks937a_serial_pr.template
DB += sync_mks937b_serial.template
DB += sync_mks937b_serial_cc.template
DB += sync_mks937b_serial_pr.template
DB += vac_mks937a_serial.template
DB += vac_mks937a_serial_cc.template
DB += vac_mks937a_serial_pr.template
DB += vac_mks937a_serial_tc.template
DB += vac_gammampc_serial_controller.template
DB += vac_gammampc_serial_pump.template
DB += vac_gammampc_serial_setpoint.template
DB += vac_cryo_ready.template
DB += vac_varianturbo_plc.template
DB += vac_varianturbo_serial.template
DB += vac_pumps_serial.db


#----------------------------------------------------
# Create and install (or just install)
# Archive files, templates, substitutions like this
#


#----------------------------------------------------
# Create and install (or just install)
# Autosave request files, templates, substitutions like this
#


# Nothing to build for autosave, just install from $AUTOSAVE/db
DB_INSTALLS += $(AUTOSAVE)/db/save_restoreStatus.db

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE

