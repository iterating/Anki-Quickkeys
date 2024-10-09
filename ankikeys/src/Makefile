CFLAGS=-g $(shell pkg-config --cflags json-c xmu)
LDFLAGS=-g $(shell pkg-config --libs json-c xmu)

all:
	$(CC) ankikeys.c $(CFLAGS) $(LDFLAGS) -lm -lpthread -o ankikeys
