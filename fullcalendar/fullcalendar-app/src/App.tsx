import React from 'react';

import FullCalendar from '@fullcalendar/react'
import dayGridPlugin from '@fullcalendar/daygrid'

import './main.css';

const App: React.FC = () => {
  return (
    <FullCalendar
        defaultView="dayGridMonth"
        plugins={[ dayGridPlugin ]}
    />
  );
}

export default App;
