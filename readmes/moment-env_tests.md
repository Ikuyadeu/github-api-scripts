This is a testbed for exposing moment to the world.

The package.sh takes the files from src/ and appends/prepends the necessary
lines to make them cjs/esm compatible, and then outputs the results in
node\_modules/bmoment (so it looks like we npm-installed it -- similar to how
our users will have it).

Then run
    
    ./package.sh
    node --version # 10.5.0
    node bmoment_test_cjs.js
    node --experimental-modules  bmoment_test_esm.mjs
