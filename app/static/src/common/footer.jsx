import React from 'react';
import SocketMixin from '../mixins/socketMixin.jsx';
import OnFireMixin from '../mixins/onFireMixin.jsx';

const Footer = React.createClass({
  mixins: [SocketMixin, OnFireMixin],  // 引入 mixin
  receiveMessage: function(message) {
    try { 
      message = JSON.parse(message);
      if (message.type && message.data) {
        //webhook_status / new_history / history_status
        console.log('fire event:', message.type, message.data);

        this.fire(message.type, message.data);
      }
    } catch (e) {}
  },
  componentDidMount: function() {
    this.readSocket('ws', this.receiveMessage);
  },
  render: function() {
    return (
      <div className="ui inverted vertical footer segment">
        <div className="ui center aligned container">
          <div className="ui horizontal inverted small divided link list">
            <span>&copy; 2016 &hearts;<a target="_blank" href="https://github.com/hustcc"> Hustcc </a>&hearts; 版权所有</span>
          </div>
        </div>
      </div>
    )
  }
});

export default Footer;