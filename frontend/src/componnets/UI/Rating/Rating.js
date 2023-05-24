import React, {useEffect, useState} from 'react';
import s from './Rating.module.css'
import FillStarSVG from "../../svg/FillStarSVG";
import PartlyFillStar from "../../svg/PartlyFillStar";
import EmptyStar from "../../svg/EmptyStar";

const Rating = ({rating}) => {

    const [stars, setStars] = useState([])

    useEffect(() => {
        let temp = []
        const totalRating = rating.toString().split('.')

        for (let i = 0; i < parseInt(totalRating[0]); i++) {
            temp.push(FillStarSVG)
        }
        if (parseInt(totalRating[1][0]) > 0) {
            temp.push(PartlyFillStar)
            for (let i = 0; i < 4 - parseInt(totalRating[0]); i++) {
                temp.push(EmptyStar)
            }
        } else {
            for (let i = 0; i < 5 - parseInt(totalRating[0]); i++) {
                temp.push(EmptyStar)
            }
        }

        setStars(temp)
    }, [])

    return (
        <div className={s.rating}>
            {stars.map((Component,count) =>
                <Component key={count}/>
            )}
        </div>
    );
};

export default Rating;