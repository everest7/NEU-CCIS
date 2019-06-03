all: server multiserver client

# define useful flags to cc/ld/etc.
CFLAGS = -g -Wall -I. -I.. -Iincludes -pthread

server: QueryServer.c
	gcc $(CFLAGS) -g  -o queryserver \
	QueryServer.c -L. libIndexer.a -L. libHtll.a

multiserver: MultiServer.c
	gcc $(CFLAGS) -g -o multiserver MultiServer.c \
	-L. libIndexer.a -L. libHtll.a

runserver:
	./queryserver data_small/ 1500

runmultiserver:
	./multiserver data_small/ 1500

client: QueryClient.c
	gcc $(CFLAGS) -g -o queryclient QueryClient.c \
	-L. libIndexer.a -L. libHtll.a

runclient:
	./queryclient 127.0.0.1 1500

clean: FORCE
	/bin/rm -f *.o *~ multiserver queryserver queryclient

FORCE:
