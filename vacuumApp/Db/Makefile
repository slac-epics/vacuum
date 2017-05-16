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

DB += sync_master.db
DB += sync_mks146c_serial.template
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
DB += vac_mks937b_serial_cc.template
DB += vac_mks937b_serial_pr.template
DB += vac_mks937b_serial.template
DB += vac_gammampc_serial_controller.template
DB += vac_gammampc_serial_pump.template
DB += vac_gammampc_serial_setpoint.template
DB += vac_cryo_ready.template
DB += vac_varianturbo_plc.template
DB += vac_varianturbo_serial.template
DB += vac_pumps_serial.db
DB += ptm_serial.db
#DB += vac_mks500_serial.template
DB += modbus_vg_state.template
DB += modbus_valve_position_state.template
DB += modbus_turboPump_state.template
DB += sync_gammampc_serial_controller.template
DB += sync_gammampc_serial_pump.template
DB += sync_gammampc_serial_setpoint.template
DB += sync_gammampc_serial.db
DB += rough_pump.template

DB += sync_varianturbo_serial.template
#----------------------------------------------------
# Create and install (or just install)
# Archive files, templates, substitutions like this
#

ARCHIVE += archive_gcc.tpl-arch
ARCHIVE += archive_gcc_937a.tpl-arch
ARCHIVE += archive_gpi.tpl-arch
ARCHIVE += archive_gpi_937a.tpl-arch
ARCHIVE += archive_gtc.tpl-arch
ARCHIVE += archive_pip.tpl-arch
ARCHIVE += archive_ptm.tpl-arch
ARCHIVE += archive_ptm-magd.tpl-arch
ARCHIVE += archive_vgc.tpl-arch
ARCHIVE += archive_rtd.tpl-arch
ARCHIVE += archive_vcn.tpl-arch
ARCHIVE += archive_ghc.tpl-arch
ARCHIVE += archive_903.tpl-arch
ARCHIVE += archive_907.tpl-arch
ARCHIVE += archive_ivcs-gcc.tpl-arch
ARCHIVE += archive_ivcs-vgc.tpl-arch
ARCHIVE += archive_ivcs-vic.tpl-arch
ARCHIVE += archive_ivcs-vg.tpl-arch

#----------------------------------------------------
# Create and install (or just install)
# Autosave request files, templates, substitutions like this
#

REQ += autosave_pip.tpl-req
REQ += autosave_gtc.tpl-req
REQ += autosave_gpi.tpl-req
REQ += autosave_gcc.tpl-req
REQ += autosave_ptm.tpl-req
REQ += autosave_ptm_fee.tpl-req
REQ += autosave_vgc.tpl-req
REQ += autosave_ivcs_vac_gauge.tpl-req
REQ += autosave_rough_pump.tpl-req

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE

