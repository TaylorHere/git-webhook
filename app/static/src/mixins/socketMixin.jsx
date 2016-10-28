let SocketMixin = {
  socketio: null,
  componentDidMount: function() {
    // socketio
    if (! this.socketio) this.socketio = io.connect(location.protocol + '//' + location.host);
  },
  componentWillUnmount: function() {
    if (this.socketio)
      this.socketio.disconnect();
    this.socketio = null;
  },
  readSocket: function(evnet, callback) {
    this.socketio.on(evnet, callback);
  }
}

export default SocketMixin;