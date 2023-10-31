// BluetoothService.js
import { BleManager } from 'react-native-ble-plx';

class BluetoothService {
  constructor() {
    this.bleManager = new BleManager();
    this.connectedDevice = null;
  }

  // Start scanning for the target Bluetooth device
  startScanning(deviceName, callback) {
    this.bleManager.startDeviceScan(null, null, (error, device) => {
      if (error) {
        console.error('Error scanning for devices:', error);
        return;
      }

      if (device.name === deviceName) {
        this.bleManager.stopDeviceScan();
        callback(device);
      }
    });
  }

  // Connect to the specified Bluetooth device
  connectToDevice(device, onConnected, onError) {
    device.connect()
      .then(connectedDevice => {
        this.connectedDevice = connectedDevice;
        console.log('Connected to device:', connectedDevice.name);
        onConnected(connectedDevice);
      })
      .catch(error => {
        console.error('Error connecting to device:', error);
        onError(error);
      });
  }

  // Disconnect from the currently connected Bluetooth device
  disconnectDevice(onDisconnected) {
    if (this.connectedDevice) {
      this.connectedDevice.cancelConnection()
        .then(() => {
          console.log('Disconnected from device:', this.connectedDevice.name);
          this.connectedDevice = null;
          onDisconnected();
        })
        .catch(error => {
          console.error('Error disconnecting from device:', error);
        });
    }
  }
}

export default BluetoothService;
