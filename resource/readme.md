# For use in Farama Foundation only

To get Roms from AutoROM in CI tests for other repositories without using torrenting:

## To use in CI

```yaml
- name: Decrypt Roms.tar.gz
  env:
    DECRYPTION_KEY: ${{ secrets.AUTOROM_DECRYPTION_KEY }}
  run: |
    wget https://raw.githubusercontent.com/FaramaFoundation/AutoROM/master/resource/Roms.tar.gz.b64.enc
    openssl aes-256-cbc -a -salt -pass pass:$DECRYPTION_KEY -in Roms.tar.gz.b64.enc -out Roms.tar.gz.b64 -d
    base64 Roms.tar.gz.b64 --decode &> Roms.tar.gz
    AutoROM --accept-license --source-file Roms.tar.gz
```

## File Storage Methodology

### Encryption

1. `base64 Roms.tar.gz &> Roms.tar.gz.b64`
2. `openssl aes-256-cbc -a -salt -pass pass:$DECRYPTION_KEY -in Roms.tar.gz.b64 -out Roms.tar.gz.b64.enc -e`

### Decryption

1. `openssl aes-256-cbc -a -salt -pass pass:$DECRYPTION_KEY -in Roms.tar.gz.b64.enc -out Roms.tar.gz.b64 -d`
2. `base64 Roms.tar.gz.b64 --decode &> Roms.tar.gz`

