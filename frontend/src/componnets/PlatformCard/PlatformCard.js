import React from 'react';
import s from './PlatformCard.module.css'
import LikeButton from "../UI/LikeButton/LikeButton";
import Rating from "../UI/Rating/Rating";

const PlatformCard = ({platform}) => {

    return (
        <div className={s.block}>
            <div className={s.block_img}>
                <LikeButton/>
                <img src={platform.image} alt=""/>
            </div>
            <div className={s.block_description}>
                <div className={s.description_content}>
                    <h3>{platform.name}</h3>
                    <div className={s.content_specifications}>
                        <p>{platform.address}</p>
                        <div className={s.specification_items}>
                            <div>
                                {platform.footage} м
                                <sup>2</sup>
                            </div>
                            <span/>
                            <div>{platform.capacity} чел.</div>
                            <span/>
                            <div>{platform.tel}</div>
                        </div>
                        <div className={s.content_info}>
                            <p>
                                <b>от {platform.price} ₽ / час</b>
                            </p>
                            <div>
                                <span>{platform.rating}</span>
                                <Rating rating={platform.rating}/>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default PlatformCard;