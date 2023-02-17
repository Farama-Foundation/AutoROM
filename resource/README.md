# For use in Farama Foundation only

To get Roms from AutoROM in CI tests for other repositories without using torrenting:

## To use in CI

```yaml
- name: Decrypt Roms.tar.gz
  env:
    ROMS_B64_LINK: ${{ secrets.ROMS_B64_LINK }}
  run: |
    wget "$ROMS_B64_LINK"
    base64 Roms.tar.gz.b64 --decode &> Roms.tar.gz
    AutoROM --accept-license --source-file Roms.tar.gz
```
