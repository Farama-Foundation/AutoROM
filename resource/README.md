# For use in Farama Foundation only

To get Roms from AutoROM in CI tests for other repositories without using torrenting:

## To use in CI

```yaml
- name: Decrypt Roms.tar.gz
  env:
    DECRYPTION_KEY: ${{ secrets.AUTOROM_DECRYPTION_KEY }}
  run: |
    wget "https://raw.githubusercontent.com/jjshoots/AutoROM/master/resource/Roms.tar.gz.b64.enc"
    openssl enc -d -aes-256-cbc -md sha256 -in Roms.tar.gz.b64.enc -out Roms.tar.gz.b64 -k "$DECRYPTION_KEY"
    base64 Roms.tar.gz.b64 --decode &> Roms.tar.gz
    AutoROM --accept-license --source-file Roms.tar.gz
```

## File Storage Methodology

### Encryption

1. `base64 Roms.tar.gz &> Roms.tar.gz.b64`
2. `openssl enc -e -aes-256-cbc -md sha256 -in Roms.tar.gz.b64 -out Roms.tar.gz.b64.enc -k "$DECRYPTION_KEY"`

### Decryption

1. `openssl enc -d -aes-256-cbc -md sha256 -in Roms.tar.gz.b64.enc -out Roms.tar.gz.b64 -k "$DECRYPTION_KEY"`
2. `base64 Roms.tar.gz.b64 --decode &> Roms.tar.gz`

