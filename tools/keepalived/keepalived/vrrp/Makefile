# Makefile
#
# Keepalived OpenSource project.
#
# Copyright (C) 2001-2012 Alexandre Cassen, <acassen@gmail.com>

CC	 = gcc
SNMP_FLAG = _WITHOUT_SNMP_
INCLUDES = -I../include -I../../lib
CFLAGS	 = -g -O2  -I/usr/src/linux/include -I/usr/src/linux/include $(INCLUDES) \
	   -Wall -Wunused -Wstrict-prototypes
CFLAGS += -I ../../../../include
DEFS	 = -D_KRNL_2_6_ -D_WITH_LVS_ -D_HAVE_IPVS_SYNCD_ -D_HAVE_VRRP_VMAC_ -D_WITHOUT_SNMP_ 
COMPILE	 = $(CC) $(CFLAGS) $(DEFS)

OBJS = 	vrrp_daemon.o vrrp_data.o vrrp_parser.o \
	vrrp.o vrrp_notify.o vrrp_scheduler.o vrrp_sync.o vrrp_index.o \
	vrrp_netlink.o vrrp_arp.o vrrp_if.o vrrp_track.o vrrp_ipaddress.o \
	vrrp_iproute.o vrrp_ipsecah.o vrrp_ndisc.o vrrp_vmac.o
ifeq ($(SNMP_FLAG),_WITH_SNMP_)
  OBJS += vrrp_snmp.o
endif
HEADERS = $(OBJS:.o=.h)

SRCS := $(shell find ./ -name '*.c' | sort)

.c.o:
	$(COMPILE) -c $<

all:	$(OBJS)

clean:
	rm -f *.a *.o *~

distclean: clean
	rm -f Makefile

vrrp_daemon.o: vrrp_daemon.c ../include/vrrp_daemon.h ../include/vrrp_scheduler.h \
  ../include/vrrp_if.h ../include/vrrp_arp.h ../include/vrrp_netlink.h ../include/vrrp_iproute.h \
  ../include/vrrp_iproute.h ../include/vrrp_parser.h ../include/vrrp_data.h \
  ../include/vrrp.h ../include/global_data.h ../include/pidfile.h ../include/daemon.h \
  ../include/ipvswrapper.h ../../lib/list.h ../../lib/memory.h ../../lib/parser.h \
  ../../lib/signals.h ../include/snmp.h ../include/vrrp_snmp.h
vrrp_data.o: vrrp_data.c ../include/vrrp_data.h \
  ../include/vrrp_sync.h ../include/vrrp_if.h ../include/vrrp_vmac.h ../include/vrrp_index.h \
  ../include/vrrp.h ../../lib/memory.h ../../lib/utils.h ../../lib/notify.h
vrrp_parser.o: vrrp_parser.c ../include/vrrp_parser.h \
  ../include/vrrp_data.h ../include/vrrp_sync.h ../include/vrrp_index.h \
  ../include/vrrp.h ../include/global_data.h ../include/global_parser.h \
  ../../lib/parser.h ../../lib/memory.h
vrrp.o: vrrp.c ../include/vrrp.h ../include/vrrp_scheduler.h \
  ../include/vrrp_notify.h ../include/ipvswrapper.h ../../lib/memory.h \
  ../../lib/list.h ../include/vrrp_data.h ../include/vrrp_sync.h ../include/vrrp_index.h \
  ../include/vrrp_arp.h ../../lib/utils.h ../include/vrrp_vmac.h ../include/snmp.h \
  ../include/vrrp_snmp.h
vrrp_notify.o: vrrp_notify.c ../include/vrrp_notify.h ../../lib/memory.h \
  ../../lib/notify.h
vrrp_scheduler.o: vrrp_scheduler.c ../include/vrrp_scheduler.h \
  ../include/vrrp_ipsecah.h ../include/vrrp_if.h ../include/vrrp_vmac.h ../include/vrrp.h \
  ../include/vrrp_sync.h ../include/vrrp_notify.h ../include/ipvswrapper.h \
  ../../lib/memory.h ../../lib/list.h ../include/vrrp_data.h ../include/vrrp_index.h \
  ../include/smtp.h ../../lib/notify.h ../include/snmp.h ../include/vrrp_snmp.h
vrrp_sync.o: vrrp_sync.c ../include/vrrp_sync.h ../include/vrrp_if.h \
  ../include/vrrp_notify.h ../include/vrrp_data.h
vrrp_index.o: vrrp_index.c ../include/vrrp_index.h ../include/vrrp.h \
  ../include/vrrp_data.h ../../lib/memory.h
vrrp_netlink.o: vrrp_netlink.c ../include/vrrp_netlink.h ../include/check_api.h \
  ../include/vrrp_if.h ../../lib/memory.h ../../lib/scheduler.h \
  ../../lib/utils.h
vrrp_arp.o: vrrp_arp.c ../include/vrrp_arp.h
vrrp_track.o: vrrp_track.c ../include/vrrp_track.h ../include/vrrp_if.h \
  ../include/vrrp_data.h ../../lib/memory.h
vrrp_if.o: vrrp_if.c ../include/vrrp_if.h ../include/vrrp_netlink.h \
  ../../lib/scheduler.h ../include/vrrp_data.h ../../lib/memory.h \
  ../../lib/utils.h
vrrp_ipaddress.o: vrrp_ipaddress.c ../include/vrrp_ipaddress.h ../include/vrrp_netlink.h \
  ../include/vrrp_if.h  ../include/vrrp_data.h ../../lib/memory.h ../../lib/utils.h
vrrp_iproute.o: vrrp_iproute.c ../include/vrrp_iproute.h ../include/vrrp_netlink.h \
  ../include/vrrp_if.h  ../include/vrrp_data.h ../../lib/memory.h ../../lib/utils.h
vrrp_ipsecah.o: vrrp_ipsecah.c ../include/vrrp_ipsecah.h
vrrp_ndisc.o: vrrp_ndisc.c ../include/vrrp_ndisc.h ../include/vrrp_ipaddress.h \
  ../../lib/utils.h ../../lib/memory.h
vrrp_vmac.o: vrrp_vmac.c ../include/vrrp_vmac.h ../include/vrrp_netlink.h \
  ../include/vrrp_data.h ../../lib/logger.h ../../lib/memory.h ../../lib/utils.h
vrrp_snmp.o: vrrp_snmp.c ../include/vrrp_snmp.h ../include/vrrp_track.h \
  ../include/vrrp_data.h ../include/vrrp_ipaddress.h ../include/vrrp_iproute.h \
  ../include/vrrp.h ../../lib/vector.h ../../lib/list.h ../include/snmp.h \
  ../include/global_data.h ../../lib/logger.h

dep:
	$(CC) $(CFLAGS) -M $(SRCS) | ../../../../scripts/mkdep.py ../../../../deps
