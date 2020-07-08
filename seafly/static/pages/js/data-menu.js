export default {
    menus: [
        {
            name: 'Notre Société',
            route: {name: 'desc', params: {name: 'about'}}
        },
        {
            name: 'Nos Services',
            sub: [
                {
                    name: 'Fret Maritime',
                    route: {name: 'desc', params: {name: 'fret-maritime'}}
                },
                {
                    name: 'Fret Aérien',
                    route: {name: 'desc', params: {name: 'fret-aerien'}}
                },
                {
                    name: 'Service lettre, petit colis express',
                    route: {name: 'desc', params: {name: 'colis-express'}}
                },
                {
                    name: 'Déménagements',
                    route: {name: 'desc', params: {name: 'demenagements-internationaux'}}
                },
                {
                    name: 'Formalités Douanières',
                    route: {name: 'desc', params: {name: 'formalites-douanieres'}}
                },
                {
                    name: 'Transport Frontalier',
                    route: {name: 'desc', params: {name: 'transports-frontaliers'}}
                },
            ]
        },
        {
            name: 'Destinations',
            sub: [
                {
                    name: 'DOM TOM',
                    route: {name: 'desc', params: {name: 'expedition-dom-tom'}}
                },
                {
                    name: 'France',
                    route: {name: 'desc', params: {name: 'expedition-france'}}
                },
                {
                    name: 'Chine',
                    route: {name: 'desc', params: {name: 'expedition-chine'}}
                },
                {
                    name: 'Expédition à l\'international',
                    route: {name: 'desc', params: {name: 'expedition-internationaux'}}
                },
            ]
        },
        {
            name: 'Promotions',
            route: {name: 'promos'}
        },
        {
            name: 'F.A.Q',
            route: {name: 'faq'}
        },
        {
            name: 'Nous Contacter',
            route: {name: 'contact'}
        }
    ]
}