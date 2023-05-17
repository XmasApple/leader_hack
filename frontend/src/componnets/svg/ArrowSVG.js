import React from "react";

function ArrowSVG() {
    return (
        <svg
            xmlns="http://www.w3.org/2000/svg"
            width="44"
            height="44"
            fill="none"
            viewBox="0 0 44 44"
        >
            <circle cx="22" cy="22" r="22" fill="#fff"/>
            <path
                fill="url(#paint0_linear_1_152)"
                d="M30.967 22.2l-8.167 7v-5.833h-10v-2.333h10v-5.833l8.167 7z"
            />
            <defs>
                <linearGradient
                    id="paint0_linear_1_152"
                    x1="12.8"
                    x2="37.2"
                    y1="22.401"
                    y2="20.001"
                    gradientUnits="userSpaceOnUse"
                >
                    <stop offset="0.182" stopColor="#5005EF"/>
                    <stop offset="0.917" stopColor="#5005EF" stopOpacity="0.26"/>
                </linearGradient>
            </defs>
        </svg>
    );
}

export default ArrowSVG;
