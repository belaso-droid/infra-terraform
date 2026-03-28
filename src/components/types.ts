// types.ts
// eslint-disable-next-line @typescript-eslint/no-explicit-any
type Maybe<T> = T | null | undefined;

// eslint-disable-next-line @typescript-eslint/no-explicit-any
type ObjectWithKeys<T> = {
  [P in keyof T]: T[P];
};

type TerraformCloudRegion = 'us' | 'eu' | 'ap' | 'ap-ac' | 'ap-jp' | 'me-sg' | 'cn' | 'cn-hongkong' | 'us-gov' | 'us-gov-washdc' | 'us-gov-ca' | 'ca-central-1' | 'uk' | 'sa';