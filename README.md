[![](https://img.shields.io/badge/akao_1.0.0-passing-green)](https://github.com/gongahkia/akao/releases/tag/1.0.0) 
![](https://github.com/gongahkia/akao/actions/workflows/scrape-to-local.yml/badge.svg)
![](https://img.shields.io/badge/akao_1.0.0-deployment_down-orange)

> [!WARNING]  
> [`Akao`](https://github.com/gongahkia/akao)'s Vercel deployment is inactive as of 23 May 2025.  

# `Akao`

[Endurance](https://www.asics.com/sg/en-sg/mk/blog/article/how-to-improve-your-endurance?srsltid=AfmBOoqOyyg9B_q6uump-LDfLZwIIo_b92mBMke0z0bg_jKd2Ul8tqqD) should be the difficult part of [cardio](https://en.wikipedia.org/wiki/Aerobic_exercise).  

Finding an [exercise route](https://www.reddit.com/r/running/comments/rx0nkz/how_do_you_find_a_route_when_you_dont_know_the/?rdt=59295) shouldn't be.

## Usage

Use the live website [***here***](https://akao-lyart.vercel.app/).

[Sites](#coverage) are scraped monthly on [SGT Monday 12am](#architecture).

> [!IMPORTANT]  
> Read the [legal disclaimer](#legal-disclaimer) before using `Akao`.  

## Rationale

As someone who runs [relatively often](./asset/reference/me.jpeg), it frustrated me how needlessly difficult it was to find suitable running routes in my area.

With that in mind, I threw together `Akao` over the period of [2 days](https://github.com/gongahkia/akao/commit/07beec228a9627be5bd0a2cccb9b84ce584ce9ef).

`Akao` simplifies the process by curating ***all vital information*** at [a glance](#screenshots) and delivering you cycling, running and walking routes *(scraped monthly from [trusted sites](#coverage))* in a single, [streamlined](https://www.oracle.com/sg/retail/omnichannel/what-is-omnichannel/) Web App.

## Stack

* *Frontend*: [Svelte](https://svelte.dev/), [Vercel](https://vercel.com/), [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
* *Backend*: [Github Actions](https://github.com/features/actions), [Python](https://www.python.org/)
* *Package*: [Docker](https://www.docker.com/)

## Screenshots

### Main page

<div style="display: flex; justify-content: space-between;">
  <img src="./asset/reference/1.png" width="49%">
</div>

### Filtering by Name, Location, Country, Activity type, Terrain type

<div style="display: flex; justify-content: space-between;">
  <img src="./asset/reference/2.png" width="49%">
  <img src="./asset/reference/3.png" width="49%">
</div>

<br>

<div style="display: flex; justify-content: space-between;">
  <img src="./asset/reference/4.png" width="49%">
  <img src="./asset/reference/5.png" width="49%">
</div>

<br>

<div style="display: flex; justify-content: space-between;">
  <img src="./asset/reference/6.png" width="49%">
</div>

## Architecture

![](./asset/reference/architecture.png)

## Coverage

`Akao` currently scrapes the following sites [monthly](#architecture).

| Site | Status | Item threshold |
| :--- | :--- | :--- |
| [Great Runs](https://greatruns.com/) | ![](https://img.shields.io/badge/Status-Supported-brightgreen) | None |
| [Outdooractive](https://www.outdooractive.com/en/) | ![](https://img.shields.io/badge/Status-Supported-brightgreen) | 100 |
| [Plotaroute](https://www.plotaroute.com/) | ![](https://img.shields.io/badge/Status-Supported-brightgreen) | 100 |
| [RunGo](https://www.rungoapp.com/) | ![](https://img.shields.io/badge/Status-Supported-brightgreen) | 100 |
| [Wikiloc](https://www.wikiloc.com/) | ![](https://img.shields.io/badge/Status-Supported-brightgreen) | 100 | 
| [Strava](https://www.strava.com/) | ![](https://img.shields.io/badge/Status-Unsupported-red) | - |
| [AllTrails](https://www.alltrails.com/) | ![](https://img.shields.io/badge/Status-Unsupported-red) | - |

## Issues

Report any issues to [gabrielzmong@gmail.com](mailto:gabrielzmong@gmail.com).

## Reference

The name `Akao` is in reference to [Rion Akao](https://sakamoto-days.fandom.com/wiki/Rion_Akao), a close friend of [Taro Sakamoto](https://sakamoto-days.fandom.com/wiki/Taro_Sakamoto) and [Yoichi Nagumo](https://sakamoto-days.fandom.com/wiki/Yoichi_Nagumo) from their time as students at [JCC](https://sakamoto-days.fandom.com/wiki/Japan_Clear_Creation). She first appears in the [Taro Sakamoto's Past Arc](https://sakamoto-days.fandom.com/wiki/Taro_Sakamoto%27s_Past_Arc) under the ongoing manga series [Sakamoto Days](https://sakamoto-days.fandom.com/wiki/Sakamoto_Days_Wiki).

<div align="center">
    <img src="./asset/logo/akao.webp">
</div>

## Legal Disclaimer

### For Informational Purposes Only

The information provided on Akao is for general informational purposes only. While we strive to ensure the accuracy and reliability of the running routes displayed, Akao makes no guarantees, representations, or warranties of any kind, express or implied, about the completeness, accuracy, reliability, suitability, or availability of the information. Users should independently verify any information before making decisions based on it.

### No Professional Advice

Akao does not provide professional fitness, health, or safety advice. The running routes displayed should not be considered as a substitute for professional advice from qualified fitness trainers or healthcare providers. Users are encouraged to consult with appropriate professionals regarding their fitness capabilities and suitability for specific routes.

### No Endorsement

The inclusion of any running routes or reference to any websites on Akao does not constitute an endorsement or recommendation of those routes or websites. Akao is not affiliated with any of the original content providers unless explicitly stated otherwise.

### Third-Party Content

Akao displays information sourced from third-party providers and websites. We do not control, monitor, or guarantee the accuracy or reliability of such third-party content. The running routes and related information are derived from publicly available sources, and Akao does not claim ownership of this content. Using information obtained from these sources is at your own risk, and Akao is not responsible for any content, claims, or damages resulting from their use.

### Use at Your Own Risk

Users access, use, and follow running routes displayed on Akao at their own risk. Running activities inherently involve physical risks, and route conditions may change without notice. Akao disclaims all liability for any loss, injury, or damage, direct or indirect, arising from reliance on the information provided on this platform. This includes but is not limited to personal injury, accidents, security incidents, environmental hazards, or decisions made based on the content displayed.

### Limitation of Liability

To the fullest extent permitted by law:

* Akao shall not be liable for any direct, indirect, incidental, consequential, or punitive damages arising out of your use of this web app or following any routes displayed on it.
* Akao disclaims all liability for errors or omissions in the content provided.
* Our total liability under any circumstances shall not exceed the amount paid by you (if any) for using Akao.

### User Responsibility

Users are solely responsible for:

* Assessing their own physical fitness and capabilities before attempting any running route.
* Being aware of their surroundings and potential hazards while running.
* Complying with all applicable laws, regulations, and rules while using public spaces.
* Obtaining necessary permissions if routes pass through private property.
* Taking appropriate safety precautions, including proper hydration, suitable attire, and awareness of weather conditions.

### Copyright and Intellectual Property

Akao respects intellectual property rights and makes efforts to only display publicly available information. If you believe your copyrighted work has been inappropriately scraped or displayed on Akao, please contact us to request its removal.

### Data Collection and Privacy

Akao may collect user data to improve service functionality. By using Akao, you consent to our data collection practices as outlined in our separate Privacy Policy.

### Changes to Content

Akao reserves the right to modify, update, or remove any content on this platform at any time without prior notice. Running routes and details may change without notice due to various factors including environmental changes, construction, or updates to source websites.

### Jurisdiction

This disclaimer and your use of Akao shall be governed by and construed in accordance with the laws of Singapore. Any disputes arising out of or in connection with this disclaimer shall be subject to the exclusive jurisdiction of the courts in Singapore.
