from datetime import datetime, timezone

print(datetime.now())
# print(datetime.utcnow())
# print(datetime.utcfromtimestamp()))

print(datetime.now(tz=timezone.utc))