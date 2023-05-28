import s from './UserCalendarCard.module.css';

const UserCalendarCard = ({ date, title }) => {
    return (
        <div className={s.calendarCard}>
            <p className={s.calendarCard_date}>{date}</p>
            <p className={s.calendarCard_title}>{title}</p>
        </div>
    );
};

export default UserCalendarCard;
