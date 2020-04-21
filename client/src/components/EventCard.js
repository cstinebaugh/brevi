import React from 'react';
import { rrulestr } from 'rrule'
import '../css/eventcard.scss';
import axios from "axios"
import MaterialIcon, {colorPalette} from 'material-icons-react';

class EventCard extends React.Component {
  constructor(props) {
    // Initialize mutable state
    super(props);
  }

  render() {
    return (
      <div>
        <div className="card-header">{this.props.headline}</div>
        <div className="event-card">
          <div className="article-chunk">
            <div className="left-header">
              Left 🐎
            </div>
            <div className="article-content">
              {this.props.leftText.map(sentence => (
                <p>{sentence}</p>
              ))}
            </div>
            <div className="bottom-link">source - <a href={this.props.leftLink}>{this.props.leftLinkName}</a></div>
          </div>
          <div className="article-chunk">
            <div className="right-header">
              Right 🐘
            </div>
            <div className="article-content">
              {this.props.rightText.map(sentence => (
                <p>{sentence}</p>
              ))}
            </div>
            <div className="bottom-link">source - <a href={this.props.rightLink}>{this.props.rightLinkName}</a></div>
          </div>
        </div>
      </div>
    );
  }
}

        export default EventCard;