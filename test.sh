ls

docker run --name artifactory --restart on-failure -d -v /arti_storage:/var/opt/jfrog/artifactory -p 8081:8081 c0935

docker run --name mongodb --restart on-failure -d -v /data/db:/data/db -p 27017:27017 65d83c

docker run --name pulse-lcm --restart on-failure --link mongodb --link artifactory --env MONGO_HOST='mongodb' --env MONGO_PORT='27017' --env ARTIFACTORY_URL='http://artifactory:8081/artifactory' --env ARTIFACTORY_USER='admin' --env ARTIFACTORY_PASSWORD='password' --env ARTIFACTORY_REPOSITORY='example-repo-local' -d -h pulse-lcm -p 8083:8083 -p 6565:6565 c3dd7c

docker run --name communication --restart on-failure --link mongodb --link pulse-lcm --env MONGO_HOST='mongodb' --env MONGO_PORT='27017' --env CAMPAIGN_HOST='pulse-lcm' --env CAMPAIGN_PORT='6565' -d -h pulseiot-communicator-service -p 50051:50051 be5cc9

docker run --name mo-service --restart on-failure --link mongodb --env MONGO_HOST='mongodb' --env MONGO_PORT='27017' --env MONGO_DATABASE='test' -d -h mo-service -p 8084:8084 6f4041

docker run -d --name pulse-envoy --restart on-failure --link pulse-lcm --link communication --link mo-service -p 3000:3000 -p 9902:9902 8cdf43
