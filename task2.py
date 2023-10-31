import React, { Component } from 'react';
import { View, Text, Button, Alert } from 'react-native';
import NfcManager, { NfcTech } from 'react-native-nfc-manager';

class NFCApp extends Component {
  constructor() {
    super();
    this.state = {
      nfcData: null,
    };
  }

  componentDidMount() {
    NfcManager.start();
    NfcManager.setEventListener(NfcTech.Ndef, this.onNfcDiscovered);
  }

  componentWillUnmount() {
    NfcManager.setEventListener(NfcTech.Ndef, null);
    NfcManager.stop();
  }

  onNfcDiscovered = async (tag) => {
    const { ndefMessage } = tag;
    if (ndefMessage && ndefMessage.length > 0) {
      const nfcData = ndefMessage[0].payload;
      this.setState({ nfcData: nfcData });
      Alert.alert('NFC Data', nfcData);
    }
  };

  render() {
    return (
      <View>
        <Text>NFC Data: {this.state.nfcData || 'No data found'}</Text>
        <Button title="Read NFC" onPress={this.readNFC} />
      </View>
    );
  }

  readNFC = () => {
    NfcManager.requestTechnology(NfcTech.Ndef)
      .then(() => {
        console.log('NFC technology enabled');
      })
      .catch((ex) => {
        console.warn(ex);
        Alert.alert('NFC Error', 'Failed to enable NFC technology');
      });
  };
}

export default NFCApp;
