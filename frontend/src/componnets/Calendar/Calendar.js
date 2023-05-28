import { useState } from 'react';
import Calendar from 'react-calendar';
import Container from '../Col/Container/Container';
import Row from '../Col/Row/Row';
import Col from '../Col/Col/Col';
import './calendar.css';

const FilterCalendar = () => {
    const [counter, setCounter] = useState(0);

    const initialMinDate = new Date();
    initialMinDate.setDate(initialMinDate.getDate() + 1);

    const [rangeDate, setRangeDate] = useState();
    const [minDate, setMinDate] = useState(initialMinDate);

    const onDateChange = (value) => {
        console.log('New date: ', value);
        setRangeDate(value);
    };

    const onClickDay = (value) => {
        setCounter((prev) => prev + 1);
        if (counter === 1) {
            setCounter(0);
            setMinDate(initialMinDate);
        } else {
            setMinDate(value);
        }
    };

    return (
        <div>
            <Calendar
                selectRange
                onChange={onDateChange}
                onClickDay={onClickDay}
                minDate={minDate}
                value={rangeDate}
            />
            <div className="reset-btn">
                <button onClick={() => setRangeDate(null)}>
                    сбросить период
                </button>
            </div>
        </div>
    );
};

export default FilterCalendar;
