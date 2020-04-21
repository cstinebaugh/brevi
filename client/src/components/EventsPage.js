import React from 'react';
import Fuse from "fuse.js";
import EventCard from './EventCard.js'
import axios from "axios"
import '../css/App.scss';
import '../css/fonts.scss'

class EventsPage extends React.Component {
  constructor(props) {
    // Initialize mutable state
    super(props);
    this.state = {articleLength: 3};
    this.handleChange = this.handleChange.bind(this);
  }

  handleChange = (event) => {
    this.setState({articleLength: event.target.value});
  }

  render() {
    return (
      <div className="top">
        <div className="card-header">Article Length: {this.state.articleLength}</div>
        <input type="range" min="1" max="5" value={this.state.articleLength} onChange={this.handleChange}></input>
        <div className="spacer"></div>
        <div className="spacer"></div>
        <div className="cards">
          <EventCard
            headline={"Trump and Fed Offer Stimulus to Blunt Economic Fallout"}
            leftText={["As the growing economic toll of the coronavirus became clearer, the White House said that it supported the idea of sending cash payments directly to Americans as part of a broader $850 billion stimulus proposal that Treasury Secretary Steven Mnuchin discussed Tuesday with Republicans on Capitol Hill.", "Mr. Mnuchin said that the Trump administration favors making direct payments quickly, noting that the effects of a payroll tax cut would take months to reach people.", "It was a shift in priority for the administration, which has been advocating a payroll tax cut, and it came as the coronavirus ground large swaths of the economy to a halt, cost an increasing number of people their jobs and sent the markets reeling. Marriott International, the giant hotel chain, said Tuesday that it is starting to furlough what it expected will be tens of thousands of employees as it closes hotel properties around the world."]} 
            rightText={["As the growing economic toll of the coronavirus became clearer, the White House said that it supported the idea of sending cash payments directly to Americans as part of a broader $850 billion stimulus proposal that Treasury Secretary Steven Mnuchin discussed Tuesday with Republicans on Capitol Hill.", "Mr. Mnuchin said that the Trump administration favors making direct payments quickly, noting that the effects of a payroll tax cut would take months to reach people.", "It was a shift in priority for the administration, which has been advocating a payroll tax cut, and it came as the coronavirus ground large swaths of the economy to a halt, cost an increasing number of people their jobs and sent the markets reeling. Marriott International, the giant hotel chain, said Tuesday that it is starting to furlough what it expected will be tens of thousands of employees as it closes hotel properties around the world."]} 
            leftLinkName={"nyTimes"} 
            leftLink={"https://abcnews.go.com/Politics/draft-cuomo-2020-groundswell-emerges-amid-york-governors/story?id=69879290"}
            rightLinkName={"abc"}
            rightLink={"https://abcnews.go.com/Politics/draft-cuomo-2020-groundswell-emerges-amid-york-governors/story?id=69879290"}
          />
          <EventCard
            headline={"Trump and Fed Offer Stimulus to Blunt Economic Fallout"}
            leftText={["As the growing economic toll of the coronavirus became clearer, the White House said that it supported the idea of sending cash payments directly to Americans as part of a broader $850 billion stimulus proposal that Treasury Secretary Steven Mnuchin discussed Tuesday with Republicans on Capitol Hill.", "Mr. Mnuchin said that the Trump administration favors making direct payments quickly, noting that the effects of a payroll tax cut would take months to reach people.", "It was a shift in priority for the administration, which has been advocating a payroll tax cut, and it came as the coronavirus ground large swaths of the economy to a halt, cost an increasing number of people their jobs and sent the markets reeling. Marriott International, the giant hotel chain, said Tuesday that it is starting to furlough what it expected will be tens of thousands of employees as it closes hotel properties around the world."]} 
            rightText={["As the growing economic toll of the coronavirus became clearer, the White House said that it supported the idea of sending cash payments directly to Americans as part of a broader $850 billion stimulus proposal that Treasury Secretary Steven Mnuchin discussed Tuesday with Republicans on Capitol Hill.", "Mr. Mnuchin said that the Trump administration favors making direct payments quickly, noting that the effects of a payroll tax cut would take months to reach people.", "It was a shift in priority for the administration, which has been advocating a payroll tax cut, and it came as the coronavirus ground large swaths of the economy to a halt, cost an increasing number of people their jobs and sent the markets reeling. Marriott International, the giant hotel chain, said Tuesday that it is starting to furlough what it expected will be tens of thousands of employees as it closes hotel properties around the world."]} 
            leftLinkName={"nyTimes"} 
            leftLink={"https://abcnews.go.com/Politics/draft-cuomo-2020-groundswell-emerges-amid-york-governors/story?id=69879290"}
            rightLinkName={"abc"}
            rightLink={"https://abcnews.go.com/Politics/draft-cuomo-2020-groundswell-emerges-amid-york-governors/story?id=69879290"}
          />
        </div>
        <div className="footer">
        </div>
      </div>
    );
  }
}

            export default EventsPage;
