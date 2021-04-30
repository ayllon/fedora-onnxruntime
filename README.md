## Instructions

Downloading the `.tar.gz` archive from github will not work because of the
external submodules.

It is better to clone locally, checkout the tag, do a `git submodule sync` and `git submodule
update`, and run `tar cz --exclude-vcs` directly.

