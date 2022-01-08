import { createClient } from "redis";
// This is a simple connection to a reddis client
(async () => {
    const client = createClient();
    //Handles if connection is errored out
    client.on("error", (err) => console.log("Redis client not connected to the server: ", err));
    // Handles if connection works between server and client
    client.on("ready", () => console.log("Redis client connected to the server"));

    await client.connect();
})();
