# For use in Farama Foundation only

To get Roms from AutoROM in CI tests for other repositories without using torrenting:

## File Storage Methodology

### Encryption

1. `base64 Roms.tar.gz &> Roms.tar.gz.b64`
2. `openssl aes-256-cbc -a -salt -pass pass:$DECRYPTION_KEY -in Roms.tar.gz.b64 -out Roms.tar.gz.b64.enc -e`

### Decryption

1. `openssl aes-256-cbc -a -salt -pass pass:$DECRYPTION_KEY -in Roms.tar.gz.b64.enc -out Roms.tar.gz.b64 -d`
2. `base64 Roms.tar.gz.b64 --decode &> Roms.tar.gz`

