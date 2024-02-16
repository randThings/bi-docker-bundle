import influxdb_client, os, time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

def main()
    token = "INFLUXDB_TOKEN"
    org = "INFLUXDB_ORG"
    url = "INFLUXDB_URL"
    bucket="test"

    write_client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)

    write_api = client.write_api(write_options=SYNCHRONOUS)
    
    for value in range(5):
    point = (
        Point("measurement1")
        .tag("tagname1", "tagvalue1")
        .field("field1", value)
    )
    write_api.write(bucket=bucket, org=org, record=point)
    time.sleep(1) # separate points by 1 second

if __name__=="__main__":
    main()