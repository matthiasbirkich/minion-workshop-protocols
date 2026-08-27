# Updating the existing repository with Working Copy (iPad)

This package is designed to be copied into the already-cloned repository `minion-workshop-protocols`.

Recommended sequence:

1. Make sure your current repository has no uncommitted changes you still need.
2. If Working Copy reports a stash, restore/review it before replacing files.
3. Unzip `SHARK-Seq_Workshop_Protocols.zip` in a location accessible to Working Copy.
4. Copy the files/folders into the root of the existing repository.
5. Do **not** remove `.git` or replace the repository itself with a new folder.
6. In Working Copy, review the diff. In particular inspect `_quarto.yml`, the PCR pages, and `figures/`.
7. Commit with a message such as `Expand protocol to full SHARK-Seq workshop`.
8. Push.
9. Check the Actions tab / GitHub Pages build if the repository uses the included workflow.

If the current repository already has its own Pages deployment workflow, compare it with `.github/workflows/publish.yml` before replacing the existing workflow.
