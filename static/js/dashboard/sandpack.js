import { SandpackClient } from "@codesandbox/sandpack-client";

const client = new SandpackClient(
    document.getElementById("preview"),
    {
        files: window.SANDBOX_FILES,
        template: "vanilla",
    }
);

// You can later update files:
client.updateFile("/index.html", "<h1>Updated</h1>");
client.updateFile("/index.js", "console.log('Updated')");