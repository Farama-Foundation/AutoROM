# For use in Farama Foundation only

To get Roms from AutoROM in CI tests for other repositories without using torrenting:

## To use in CI

```yaml
- name: Decrypt Roms.tar.gz
  env:
    DECRYPTION_KEY: ${{ secrets.AUTOROM_DECRYPTION_KEY }}
  run: |
    wget "https://raw.githubusercontent.com/jjshoots/AutoROM/master/resource/Roms.tar.gz.enc.b64"
    base64 Roms.tar.gz.enc.b64 --decode &> Roms.tar.gz.enc
    openssl enc -d -aes-256-cbc -md sha256 -in Roms.tar.gz.enc -out Roms.tar.gz -k "$DECRYPTION_KEY"
    AutoROM --accept-license --source-file Roms.tar.gz
```

## File Storage Methodology

### Encryption

```
openssl enc -e -aes-256-cbc -md sha256 -in Roms.tar.gz -out Roms.tar.gz.enc -k "$DECRYPTION_KEY"
base64 Roms.tar.gz.enc &> Roms.tar.gz.enc.b64
```

### Decryption

```
base64 Roms.tar.gz.enc.b64 --decode &> Roms.tar.gz.enc
openssl enc -d -aes-256-cbc -md sha256 -in Roms.tar.gz.enc -out Roms.tar.gz -k "$DECRYPTION_KEY"
```

