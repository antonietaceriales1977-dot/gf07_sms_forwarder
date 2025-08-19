      - name: Install Android SDK & NDK
        run: |
          mkdir -p $HOME/android-sdk
          cd $HOME/android-sdk
          curl -o commandlinetools.zip https://dl.google.com/android/repository/commandlinetools-linux-9477386_latest.zip
          unzip -q commandlinetools.zip -d cmdline-tools
          mkdir -p cmdline-tools/latest
          mv cmdline-tools/cmdline-tools/* cmdline-tools/latest/

          # Install required components
          yes | cmdline-tools/latest/bin/sdkmanager --licenses
          cmdline-tools/latest/bin/sdkmanager \
            "platform-tools" \
            "platforms;android-31" \
            "build-tools;31.0.0" \
            "ndk;23.1.7779620"

          # Export paths
          echo "ANDROIDSDK=$HOME/android-sdk" >> $GITHUB_ENV
          echo "ANDROIDNDK=$HOME/android-sdk/ndk/23.1.7779620" >> $GITHUB_ENV
          echo "$HOME/android-sdk/platform-tools" >> $GITHUB_PATH
          echo "$HOME/android-sdk/build-tools/31.0.0" >> $GITHUB_PATH
