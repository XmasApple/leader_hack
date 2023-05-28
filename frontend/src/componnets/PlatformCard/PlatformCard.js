import React from 'react';
import s from './PlatformCard.module.css'
import LikeButton from "../UI/LikeButton/LikeButton";
import Rating from "../UI/Rating/Rating";

const PlatformCard = ({platform, onClick}) => {

    return (
        <div
            className={s.block}>
            <div className={s.block_img}>
                <LikeButton/>
                <img onClick={onClick} src={`data:image/png;base64,${platform.image}`} alt=""/>
            </div>
            <div onClick={onClick} className={s.block_description}>
                <div className={s.description_content}>
                    <h4>{platform.name}</h4>
                    <div className={s.content_specifications}>
                        <p>{platform.platform_address}</p>
                        <div className={s.specification_items}>
                            <div>
                                {platform.square} м
                                <sup>2</sup>
                            </div>
                            <span/>
                            <div>{platform.people_capacity} чел.</div>
                            <span/>
                            <div>{platform.tel}</div>
                        </div>
                        <div className={s.content_info}>
                            <p>
                                <b>от {platform.price_per_time} ₽ / час</b>
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