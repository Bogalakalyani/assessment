import React, { Component } from 'react';
import { View, Text, Button } from 'react-native';
import { NativeModules } from 'react-native';

const { ThirdPartySDK } = NativeModules;

class ThirdPartySDKIntegration extends Component {
  constructor() {
    super();
    this.state = {
      sdkInitialized: false,
    };
  }

  initializeThirdPartySDK = async () => {
    try {
      await ThirdPartySDK.initializeAPI();
      this.setState({ sdkInitialized: true });
    } catch (error) {
      console.error('Error initializing ThirdPartySDK:', error);
    }
  };

  performSDKAction = async () => {
    if (this.state.sdkInitialized) {
      try {
        const result = await ThirdPartySDK.doSomething('exampleParameter');
        console.log('ThirdPartySDK action result:', result);
      } catch (error) {
        console.error('Error performing ThirdPartySDK action:', error);
      }
    } else {
      console.warn('ThirdPartySDK not initialized. Please initialize first.');
    }
  };

  render() {
    return (
      <View>
        <Text>ThirdPartySDK Integration</Text>
        <Button title="Initialize SDK" onPress={this.initializeThirdPartySDK} />
        <Button title="Perform SDK Action" onPress={this.performSDKAction} />
      </View>
    );
  }
}

export default ThirdPartySDKIntegration;
